# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-27 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalRoom', '0002_auto_20171222_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaluser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ваше имя'),
        ),
        migrations.AlterField(
            model_name='additionaluser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ваша фамилия'),
        ),
    ]
