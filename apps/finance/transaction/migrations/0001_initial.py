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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('transaction_amount', models.FloatField(verbose_name='İşlem Tutarı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeTransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeTransactionTypeTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.EmployeeTransactionType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('transaction_amount', models.FloatField(verbose_name='İşlem Tutarı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentTransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentTransactionTypeTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.StudentTransactionType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='studenttransaction',
            name='student_action_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.StudentTransactionType', verbose_name='İşlem Türü'),
        ),
        migrations.AddField(
            model_name='studenttransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AddField(
            model_name='employeetransaction',
            name='employee_action_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.EmployeeTransactionType', verbose_name='İşlem Türü'),
        ),
        migrations.AddField(
            model_name='employeetransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]
