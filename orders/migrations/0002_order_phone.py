# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=380, max_length=250, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]