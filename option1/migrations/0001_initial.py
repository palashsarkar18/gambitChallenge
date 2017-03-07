# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 13:18
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='humanReadableData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetimestamp', models.DateTimeField(null=True)),
                ('dataset', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='modbusData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetimestamp', models.DateTimeField(null=True)),
                ('dataset', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
