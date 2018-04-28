# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-28 08:55
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20180427_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, default=None, editable=False, null=True, populate_from='subject', unique=True),
        ),
    ]
