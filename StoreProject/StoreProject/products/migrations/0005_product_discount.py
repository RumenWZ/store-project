# Generated by Django 4.0.4 on 2022-05-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
