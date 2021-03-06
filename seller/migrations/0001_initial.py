# Generated by Django 4.0.3 on 2022-03-08 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_alter_customer_table_alter_seller_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='products/')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
