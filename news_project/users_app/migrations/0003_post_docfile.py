# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20160226_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='docfile',
            field=models.FileField(default=1, upload_to='documents/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]