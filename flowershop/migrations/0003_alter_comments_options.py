# Generated by Django 5.0 on 2023-12-21 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0002_rename_published_date_comments_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Коментарі'},
        ),
    ]