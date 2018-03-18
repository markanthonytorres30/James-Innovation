from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_imei = models.BigIntegerField(default= 0)
    product_price = models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self):
        return self.product_name

class Category(models.Model):
    category_num = models.IntegerField(default=1)
    category_name = models.CharField(max_length = 100)
    category_description = models.CharField(max_length=500)
    def __str__(self):
       return self.category_name
