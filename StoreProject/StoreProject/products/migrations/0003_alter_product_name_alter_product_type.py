# Generated by Django 4.0.4 on 2022-05-02 12:58

import StoreProject.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(5), StoreProject.common.validators.validate_only_letters_and_numbers]),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('Shirt', 'Shirt'), ('Pants', 'Pants'), ('Sweater', 'Sweater'), ('Jacket', 'Jacket'), ('Jeans', 'Jeans'), ('Dress', 'Dress'), ('Suit', 'Suit'), ('Hoodie', 'Hoodie'), ('Coat', 'Coat')], default='Shirt', max_length=7, null=True),
        ),
    ]
