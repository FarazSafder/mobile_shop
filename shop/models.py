from django.db import models

# Create your models here.

class Brands(models.Model):
    name=models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.name


class Supplier(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255,blank=True)
    phone=models.CharField(max_length=11,blank=True)

    def __str__(self):
        return self.name


class MobileModel(models.Model):
    name=models.CharField(max_length=100)
    base_price=models.DecimalField(max_digits=10,decimal_places=2)
    selling_price=models.DecimalField(max_digits=10,decimal_places=2)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE,related_name='models')
    supplier=models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True,related_name="supplied_stock")

    def __str__(self):
        return f"{self.brand.name} {self.name}"

class StockItem(models.Model):
    mobile_model=models.ForeignKey(MobileModel,on_delete=models.CASCADE,related_name="mobile")
    imei = models.CharField(max_length=15, unique=True)
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Defective', 'Defective')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"{self.mobile_model.name} - IMEI: {self.imei}"


class Sale(models.Model):
    stock_item = models.OneToOneField(StockItem, on_delete=models.PROTECT)
    customer_name = models.CharField(max_length=255)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sale: {self.stock_item.imei} to {self.customer_name}"