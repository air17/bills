from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin
from .filters import BillFilter
from .models import Bill
from .serializers import BillSerializer, BillCreateSerializer


class BillViewSet(ReadOnlyModelViewSet, CreateModelMixin):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filterset_class = BillFilter
    parser_classes = (FormParser, MultiPartParser)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BillCreateSerializer
        else:
            return BillSerializer
