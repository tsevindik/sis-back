# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('name', models.CharField(max_length=150, verbose_name='İsim')),
                ('abbreviation', models.CharField(max_length=10, verbose_name='Kısaltma')),
                ('out_of_grade', models.IntegerField(verbose_name='Not Üzerinden')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
