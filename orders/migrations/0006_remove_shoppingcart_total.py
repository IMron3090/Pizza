# Generated by Django 3.0.5 on 2020-04-25 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200425_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='total',
        ),
    ]
