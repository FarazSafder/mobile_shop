from rest_framework import serializers
from .models import Brands, Supplier, MobileModel, StockItem, Sale

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class MobileModelSerializer(serializers.ModelSerializer):

    brand_name = serializers.CharField(source='brand.name', read_only=True)
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = MobileModel
        fields = [
            'id', 'name', 'base_price', 'selling_price', 
            'brand', 'brand_name', 
            'supplier', 'supplier_name'
        ]

class StockItemSerializer(serializers.ModelSerializer):

    mobile_name = serializers.CharField(source='mobile_model.name', read_only=True)
    brand_name = serializers.CharField(source='mobile_model.brand.name', read_only=True)

    class Meta:
        model = StockItem
        fields = [
            'id', 'imei', 'status', 
            'mobile_model', 'mobile_name', 'brand_name'
        ]

class SaleSerializer(serializers.ModelSerializer):

    imei = serializers.CharField(source='stock_item.imei', read_only=True)
    model_name = serializers.CharField(source='stock_item.mobile_model.name', read_only=True)

    class Meta:
        model = Sale
        fields = [
            'id', 'stock_item', 'imei', 'model_name', 
            'customer_name', 'sale_price','date'
        ]

    def validate_stock_item(self, value):
        if value.status == 'Sold':
            raise serializers.ValidationError("This phone has already been sold.")
        if value.status == 'Defective':
            raise serializers.ValidationError("Cannot sell a defective phone.")
        if value.status != 'Available':
            raise serializers.ValidationError(f"Phone is not available. Current status: {value.status}")
        return value

    def create(self, validated_data):
        # Save the actual Sale record
        sale = super().create(validated_data)
        
        stock_item = sale.stock_item
        stock_item.status = 'Sold'
        stock_item.save()
        
        return sale