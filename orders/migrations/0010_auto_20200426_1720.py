# Generated by Django 3.0.5 on 2020-04-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200426_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='approved',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
