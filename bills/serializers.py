from io import StringIO

from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, FileField, Serializer
from .models import Bill
from .services import get_bills_from_csv


class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        exclude = ("id",)


class BillCreateSerializer(Serializer):
    file = FileField(write_only=True)

    @staticmethod
    def create(validated_data):
        file = validated_data["file"]
        decoded_file = file.read().decode('utf-8')
        io_string = StringIO(decoded_file)
        bills = get_bills_from_csv(io_string)
        try:
            instances = Bill.objects.bulk_create(bills)
        except IntegrityError as e:
            raise ValidationError(e)
        return instances
