# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 17:10
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20151212_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Measurement')),
            ],
        ),
    ]