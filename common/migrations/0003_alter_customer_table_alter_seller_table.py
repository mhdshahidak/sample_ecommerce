# Generated by Django 4.0.3 on 2022-03-04 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_seller'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='seller',
            table='seller',
        ),
    ]
