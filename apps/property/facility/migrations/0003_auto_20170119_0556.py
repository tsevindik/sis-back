# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 05:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_auto_20170118_1943'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='buildingroomtrans',
            index_together=set([('neutral', 'language_code')]),
        ),
        migrations.AlterIndexTogether(
            name='buildingtypetrans',
            index_together=set([('neutral', 'language_code')]),
        ),
        migrations.AlterIndexTogether(
            name='campusblocktrans',
            index_together=set([('neutral', 'language_code')]),
        ),
        migrations.AlterIndexTogether(
            name='campusbuildingtrans',
            index_together=set([('neutral', 'language_code')]),
        ),
        migrations.AlterIndexTogether(
            name='roomtypetrans',
            index_together=set([('neutral', 'language_code')]),
        ),
        migrations.AlterIndexTogether(
            name='universitycampustrans',
            index_together=set([('neutral', 'language_code')]),
        ),
    ]
