# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('postcode', models.IntegerField(verbose_name='Posta Kodu')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('description', models.TextField(verbose_name='Açıklama')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('number', models.CharField(max_length=30, verbose_name='Numara')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('id_no', models.CharField(max_length=20, verbose_name='Kimlik Numarası')),
                ('pass_no', models.CharField(max_length=20, verbose_name='Pasaport Numarası')),
                ('is_graduated', models.BooleanField(verbose_name='Mezun')),
                ('is_suspended', models.BooleanField(verbose_name='Kayıt Dondurdu')),
                ('is_quit', models.BooleanField(verbose_name='Ayrıldı')),
                ('gpa', models.FloatField(verbose_name='Ortalama')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('unit_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.UnitProgram', verbose_name='Program')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
