# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockBuilding',
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
            name='BuildingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('code', models.CharField(max_length=20, verbose_name='Kod')),
                ('floor', models.IntegerField(verbose_name='Kat')),
                ('capacity', models.IntegerField(verbose_name='Kapasite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BuildingRoomTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.BuildingRoom')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BuildingType',
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
            name='BuildingTypeTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.BuildingType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('postcode', models.IntegerField(verbose_name='Posta Kodu')),
                ('has_blocks', models.BooleanField(verbose_name='Blok')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Region', verbose_name='İlçe')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampusBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Campus', verbose_name='Kampüs')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampusBlockTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.CampusBlock')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampusBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('postcode', models.IntegerField(verbose_name='Posta Kodu')),
                ('has_address', models.BooleanField(verbose_name='Adres')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Campus', verbose_name='Kampüs')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Region', verbose_name='İlçe')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.BuildingType', verbose_name='Bina Türü')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampusBuildingTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.CampusBuilding')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomType',
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
            name='RoomTypeTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.RoomType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UniversityCampusTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Zamanı')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('name', models.CharField(max_length=150, verbose_name='İsim')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Language', verbose_name='Dil')),
                ('neutral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Campus')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='buildingroom',
            name='campus_building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.CampusBuilding', verbose_name='Kampüs Binası'),
        ),
        migrations.AddField(
            model_name='buildingroom',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.BuildingType', verbose_name='Bina Türü'),
        ),
        migrations.AddField(
            model_name='blockbuilding',
            name='campus_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.CampusBlock', verbose_name='Kampüs Bloğu'),
        ),
        migrations.AddField(
            model_name='blockbuilding',
            name='campus_building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.CampusBuilding', verbose_name='Kampüs Binası'),
        ),
    ]
