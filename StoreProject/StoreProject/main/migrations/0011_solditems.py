# Generated by Django 4.0.4 on 2022-06-16 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_actual_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_sales_customer_sales_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sales')),
            ],
        ),
    ]
