from django.db import models

from common.models import Seller



class AddProducts(models.Model):
    p_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    stock = models.IntegerField()

    class meta:
        db_table = "product"
