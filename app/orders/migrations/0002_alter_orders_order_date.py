# Generated by Django 3.2.2 on 2022-05-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
