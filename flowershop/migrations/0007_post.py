# Generated by Django 5.0 on 2023-12-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0006_alter_comments_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Опис')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата та час')),
                ('poster', models.URLField(default='http://placehold.it/900x300', verbose_name='Постер')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
            },
        ),
    ]
