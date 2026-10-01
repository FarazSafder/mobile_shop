from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
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

    @action(detail=False,methods=['get'],url_path='get-by-imei')
    def get_by_imei(self, request):

        imei_query = request.query_params.get('imei', None)

        if not imei_query:
            return Response({"error": "Please provide an IMEI number."}, status=400)

        try:
            stock_item = StockItem.objects.get(imei=imei_query)
            serializer = self.get_serializer(stock_item)
            data = serializer.data
            data['suggested_price'] = stock_item.mobile_model.selling_price
            return Response(data)
        except StockItem.DoesNotExist:
            raise NotFound(detail="Phone with this IMEI not found in inventory.")


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer