# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmd', '0003_auto_20170615_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now_add=True,verbose_name='\u53d1\u5e03\u65f6\u95f4'),
            preserve_default=False,
        ),
    ]
