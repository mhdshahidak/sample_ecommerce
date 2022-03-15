from django.db import models

# Create your models here.


class Customer(models.Model):

    # setting customer id as primary key (if it not enterde it will generate automaticly)
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=30)

    class Meta:  # to set table name
        db_table = "customer"


class Seller(models.Model):  # inherit from Model class

    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=30)
    acc_holder = models.CharField(max_length=20)
    acc_no = models.CharField(max_length=12)
    ifsc = models.CharField(max_length=7)
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "seller"
