from django.contrib import admin
from .models import Brands, Supplier, MobileModel, StockItem, Sale

# Register your models here.
admin.site.register(Brands)
admin.site.register(Supplier)
admin.site.register(MobileModel)
admin.site.register(StockItem)
admin.site.register(Sale)