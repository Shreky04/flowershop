# Generated by Django 5.0 on 2023-12-28 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0009_post_poster_delete_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogposter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogpics')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowershop.blogposter', verbose_name='Фото'),
        ),
    ]
