# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('section', '0001_initial'),
        ('demand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentquotademand',
            name='course_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.CourseSection', verbose_name='Ders Grubu'),
        ),
    ]
