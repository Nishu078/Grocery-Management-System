# Generated by Django 4.2.3 on 2023-08-08 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cart_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='is_paid',
        ),
    ]
