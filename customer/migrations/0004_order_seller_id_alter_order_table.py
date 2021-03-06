# Generated by Django 4.0.3 on 2022-03-11 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_customer_table_alter_seller_table'),
        ('customer', '0003_order_order_date_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seller_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='common.seller'),
        ),
        migrations.AlterModelTable(
            name='order',
            table='orders',
        ),
    ]
