# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-30 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_ad_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Ads'},
        ),
        migrations.AddField(
            model_name='ad',
            name='is_vip',
            field=models.BooleanField(default=False, verbose_name='Is VIP'),
        ),
    ]
