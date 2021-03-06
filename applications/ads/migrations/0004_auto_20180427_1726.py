# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-27 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20180415_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='ad',
            name='image',
        ),
        migrations.AddField(
            model_name='adimagemodel',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ads.Ad'),
        ),
    ]
