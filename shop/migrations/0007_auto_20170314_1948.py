# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20170313_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='tovar_slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tovar_inphoto',
            name='tovarinphoto_slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]