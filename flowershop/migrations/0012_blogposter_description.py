# Generated by Django 5.0 on 2023-12-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0011_rename_poster_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogposter',
            name='description',
            field=models.CharField(blank=True, max_length=80, verbose_name='Опис'),
        ),
    ]
