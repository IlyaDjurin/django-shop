# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_nepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategory_name', models.CharField(db_index=True, max_length=200)),
                ('kategory_slug', models.SlugField(max_length=200, unique=True)),
                ('kategory_info', models.TextField(blank=True, verbose_name='Описание')),
                ('kategory_image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение категории')),
            ],
            options={
                'ordering': ['kategory_name'],
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovar_name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('tovar_slug', models.SlugField(max_length=200)),
                ('tovar_info', models.TextField(blank=True, verbose_name='Описание')),
                ('tovar_image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара')),
                ('tovar_made', models.CharField(max_length=200)),
                ('tovar_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('tovar_url', models.CharField(max_length=200)),
                ('tovar_stock', models.PositiveIntegerField(verbose_name='На складе')),
                ('tovar_available', models.BooleanField(default=True, verbose_name='Доступен')),
                ('tovar_created', models.DateTimeField(auto_now_add=True)),
                ('tovar_updated', models.DateTimeField(auto_now=True)),
                ('kategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tovars', to='shop.Kategor', verbose_name='Категория')),
            ],
            options={
                'ordering': ['tovar_name'],
            },
        ),
        migrations.CreateModel(
            name='Tovar_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovar_name', models.CharField(db_index=True, default=None, max_length=200, verbose_name='Название товара')),
                ('tovar_image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара')),
            ],
        ),
        migrations.CreateModel(
            name='Tovar_inphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovarinphoto_slug', models.SlugField(max_length=200)),
                ('tovarinphoto_info', models.TextField(blank=True, verbose_name='Описание')),
                ('tovarinphoto_proizv', models.CharField(max_length=200, verbose_name='Производитель(фирма)')),
                ('tovarinphoto_diagon', models.CharField(max_length=200, verbose_name='Диагональ')),
                ('tovarinphoto_ram', models.CharField(max_length=200, verbose_name='Оперативная память')),
                ('tovarinphoto_akb', models.CharField(max_length=200, verbose_name='Емкость акумулятора')),
                ('tovarinphoto_osnkamera', models.CharField(max_length=200, verbose_name='Основная камера Мпс')),
                ('tovarinphoto_opsystem', models.CharField(max_length=200, verbose_name='Операционная система')),
                ('tovarinphoto_color', models.CharField(max_length=200, verbose_name='Цвет товара')),
                ('tovarinphoto_cpu', models.CharField(max_length=200, verbose_name='Процессор')),
                ('tovarinphoto_razreshenie', models.CharField(max_length=200, verbose_name='Разрешение дисплея')),
                ('tovarinphoto_frontkamera', models.CharField(max_length=200, verbose_name='Фронтальная камера Мпс')),
                ('tovarinphoto_scaner', models.CharField(max_length=200, verbose_name='Сканер отпечатка пальца')),
                ('tovarinphoto_3g', models.CharField(max_length=200, verbose_name='Наличие 3g LTE GPRS технологии')),
                ('tovarinphoto_gps', models.CharField(max_length=200, verbose_name='Поддерживаемые системы навигации,спутники')),
                ('tovarinphoto_matrix', models.CharField(max_length=200, verbose_name='Тип матрицы')),
                ('tovar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='haraktertovar', to='shop.Tovar', verbose_name='Товар')),
            ],
            options={
                'ordering': ['tovarinphoto_proizv'],
            },
        ),
        migrations.RemoveField(
            model_name='nepost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='nepost',
            name='question',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Nepost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovarinphoto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phototovar', to='shop.Tovar_inphoto', verbose_name='Фото товара'),
        ),
        migrations.AlterIndexTogether(
            name='tovar_inphoto',
            index_together=set([('id', 'tovarinphoto_slug')]),
        ),
        migrations.AlterIndexTogether(
            name='tovar',
            index_together=set([('id', 'tovar_slug')]),
        ),
    ]