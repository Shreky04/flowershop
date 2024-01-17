# Generated by Django 5.0 on 2024-01-14 19:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0019_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_method',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Желаемая дата доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(default='12:00', verbose_name='Желаемое время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='apartment',
            field=models.CharField(default=1, max_length=10, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='house',
            field=models.CharField(default=1, max_length=10, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowershop.item', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(default=1, max_length=100, verbose_name='Улица'),
        ),
    ]
