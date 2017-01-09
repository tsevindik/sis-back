# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.CourseSection', verbose_name='Ders Grubu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
