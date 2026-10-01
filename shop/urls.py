from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BrandViewSet, 
    SupplierViewSet, 
    MobileModelViewSet, 
    StockItemViewSet, 
    SaleViewSet
)

router = DefaultRouter()


router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'models', MobileModelViewSet, basename='mobilemodel')
router.register(r'stock', StockItemViewSet, basename='stockitem')
router.register(r'sales', SaleViewSet, basename='sale')


urlpatterns = [
    path('', include(router.urls)),
]