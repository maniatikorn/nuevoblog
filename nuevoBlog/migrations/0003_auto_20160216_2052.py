# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuevoBlog', '0002_auto_20160216_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='articulo',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]