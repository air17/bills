from django_filters import rest_framework as filters
from .models import Bill


class BillFilter(filters.FilterSet):
    client_name = filters.CharFilter(lookup_expr="contains")
    client_org = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Bill
        fields = ("client_name", "client_org")
