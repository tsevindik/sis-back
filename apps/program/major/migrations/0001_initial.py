# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 07:49
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
            name='MajorApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('is_approved', models.BooleanField(verbose_name='Onaylandı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MajorProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('major_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major_program', to='program.UnitProgram', verbose_name='Anadal Programı')),
                ('unit_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.UnitProgram', verbose_name='Program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='majorapplication',
            name='major_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.MajorProgram', verbose_name='Program'),
        ),
    ]
