# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-05 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180123_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]