# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='İsim')),
                ('description', models.TextField(verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicUnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
            ],
        ),
        migrations.AddField(
            model_name='academicunit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.AcademicUnitType'),
        ),
        migrations.AddField(
            model_name='academicunit',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.University'),
        ),
    ]