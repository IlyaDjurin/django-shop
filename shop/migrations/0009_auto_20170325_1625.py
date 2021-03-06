# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_tovar_inphoto_tovarinphoto_sim'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image1',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара1'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image10',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара10'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image2',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара2'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image3',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара3'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image4',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара4'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image5',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара5'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image6',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара6'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image7',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара7'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image8',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара8'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image9',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара9'),
        ),
    ]
