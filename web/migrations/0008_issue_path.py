# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-27 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20181225_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='path',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='更新的文件'),
        ),
    ]