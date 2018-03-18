from django.db import models
from products.models import Product
from inventory.models import Location
from users.models import Users

# Create your models here.
class SalesStatus(models.Model):
    status_name = models.CharField(max_length = 10)

class Sales(models.Model):
    sales_num = models.IntegerField(default=1)
    sales_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    sales_status = models.ForeignKey(SalesStatus,on_delete=models.CASCADE)
    sales_date = models.DateTimeField(auto_now=True)
    sales_cashier = models.ForeignKey(Users,on_delete=models.CASCADE)

class Discount(models.Model):
    discount_code = models.CharField(max_length=10)
    discount_value = models.DecimalField(max_digits=5,decimal_places=2)
    discount_validity = models.DateField(auto_now=True)
    discount_terms = models.CharField(max_length=800)
    discount_manager = models.ForeignKey(Users,on_delete=models.CASCADE)


class Record(models.Model):
    record_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    record_sales = models.ForeignKey(Sales,on_delete=models.CASCADE)
    record_quantity = models.IntegerField(default=1)
    record_discount = models.ForeignKey(Discount,on_delete=models.CASCADE)





