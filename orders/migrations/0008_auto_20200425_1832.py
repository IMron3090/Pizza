# Generated by Django 3.0.5 on 2020-04-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_userorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorders',
            name='orders',
            field=models.CharField(max_length=10000),
        ),
    ]
