from rest_framework import viewsets
from .models import Brands, Supplier, MobileModel, StockItem, Sale
from .serializers import (
    BrandSerializer, 
    SupplierSerializer, 
    MobileModelSerializer, 
    StockItemSerializer, 
    SaleSerializer
)

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class MobileModelViewSet(viewsets.ModelViewSet):
    queryset = MobileModel.objects.all()
    serializer_class = MobileModelSerializer

class StockItemViewSet(viewsets.ModelViewSet):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer