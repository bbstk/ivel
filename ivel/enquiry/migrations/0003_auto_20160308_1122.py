# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0002_auto_20160308_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
