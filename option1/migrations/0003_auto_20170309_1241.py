# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 12:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('option1', '0002_auto_20170308_1122'),
    ]

    operations = [
        migrations.DeleteModel(
            name='humanReadableDataTable',
        ),
        migrations.RenameField(
            model_name='modbusdatatable',
            old_name='dataset',
            new_name='machineData',
        ),
        migrations.AddField(
            model_name='modbusdatatable',
            name='humanData',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]