# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20170116_0804'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assignmenttypetrans',
            unique_together=set([('neutral', 'language_code')]),
        ),
    ]
