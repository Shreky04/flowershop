# Generated by Django 5.0 on 2024-01-14 22:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0021_remove_order_delivery_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_time',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупець'),
        ),
        migrations.AlterField(
            model_name='order',
            name='house',
            field=models.CharField(default=1, max_length=10, verbose_name='Дім'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата і час замовлення'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Кількість'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(default=1, max_length=100, verbose_name='Вулиця'),
        ),
    ]
