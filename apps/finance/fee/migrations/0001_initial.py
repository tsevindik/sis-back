# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramCreditFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('fee', models.PositiveIntegerField(verbose_name='Ücret')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramTuitionFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('fee', models.PositiveIntegerField(verbose_name='Ücret')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
