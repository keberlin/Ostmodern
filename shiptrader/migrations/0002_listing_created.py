# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiptrader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
