# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_tovar_img_tovar_info5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar_img',
            name='tovar_created',
        ),
        migrations.RemoveField(
            model_name='tovar_img',
            name='tovar_updated',
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_image11',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара11'),
        ),
        migrations.AddField(
            model_name='tovar_img',
            name='tovar_video',
            field=models.CharField(default='youtube', max_length=200),
            preserve_default=False,
        ),
    ]
