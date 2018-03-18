from django.db import models

from products.models import Product


# Create your models here.
class Location(models.Model):
    location_id = models.IntegerField(default =1)
    location_name = models.CharField(max_length = 200)
    location_address = models.CharField(max_length = 500)

class Inventory(models.Model):
    inventory_imei = models.ForeignKey(Product,on_delete=models.CASCADE)
    inventory_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    inventory_quantity = models.IntegerField(default=1)
    inventory_order = models.IntegerField(default = 5)





