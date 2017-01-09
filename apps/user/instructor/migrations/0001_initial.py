# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('user', '0002_auto_20170109_1241'),
        ('student', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('postcode', models.IntegerField(verbose_name='Posta Kodu')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Region', verbose_name='İlçe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstructorPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('number', models.CharField(max_length=30, verbose_name='Numara')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstructorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('id_no', models.CharField(max_length=20, verbose_name='Kimlik Numarası')),
                ('pass_no', models.CharField(max_length=20, verbose_name='Pasaport Numarası')),
                ('time_status', models.CharField(choices=[(0, 'Tam Zamanlı'), (1, 'Yarı Zamanlı')], max_length=1, verbose_name='Zaman Durumu')),
                ('work_hour', models.IntegerField(verbose_name='Çalışma Saati')),
                ('on_leave', models.BooleanField(verbose_name='İzinli')),
                ('is_quit', models.BooleanField(verbose_name='Ayrıldı')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
                ('work_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.WorkStatus', verbose_name='Çalışma Durumu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramAdviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('student_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentProgram', verbose_name='Öğrenci Programı')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
