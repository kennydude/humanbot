# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.IntegerField()),
                ('source_name', models.CharField(default=b'manual', max_length=50)),
                ('source_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('factor', models.IntegerField(help_text=b'\nWhat is the factor of this measurement in order to standardise it.<br/>\nFor example: "Length of pool" here may have a factor of\n25, so another pool of 50 will not skew measurements wildly\n')),
            ],
        ),
        migrations.AddField(
            model_name='measurement',
            name='grouping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.MeasurementGroup'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='human',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Human'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='measurement_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.MeasurementType'),
        ),
    ]
