import csv
from datetime import datetime
from decimal import InvalidOperation, Decimal
from typing import Iterable

from .models import Bill


def get_bills_from_csv(file: Iterable[str]) -> list[Bill]:
    """Returns correct bills from a csv file"""
    bills = []
    file_reader = csv.reader(file, delimiter=",", quotechar="|")
    for row in file_reader:
        client_name = row[0]
        client_org = row[1]
        if not (client_name or client_org):
            continue

        try:
            bill_number = int(row[2])
            bill_sum = Decimal(row[3].replace(",", "."))
            date = datetime.strptime(row[4], "%d.%m.%Y")
        except (ValueError, InvalidOperation):
            continue

        service = row[5]
        if not service or service == "-":
            continue

        bill = Bill(
            client_name=client_name,
            client_org=client_org,
            number=bill_number,
            sum=bill_sum,
            date=date,
            service=service,
        )
        bills.append(bill)

    return bills
