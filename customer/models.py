from django.db import models
from common.models import Customer

from owner.views import customer
from seller.models import Products

# Create your models here.
class Cart(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)

    class Meta:
        db_table ='cart'