# Generated by Django 4.0.4 on 2022-07-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_solditems_picture_solditems_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='solditems',
            name='name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solditems',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
