# Generated by Django 5.0 on 2024-01-14 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0020_alter_order_options_remove_order_delivery_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_date',
        ),
    ]
