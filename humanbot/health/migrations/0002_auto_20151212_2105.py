# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='measurement',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='grouping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.MeasurementGroup'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='measurement_for',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='health.MeasurementFor'),
            preserve_default=False,
        ),
    ]
