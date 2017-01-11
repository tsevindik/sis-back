# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('section', '0001_initial'),
        ('registry', '0001_initial'),
        ('assignment', '0002_auto_20170111_0908'),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionlettergrade',
            name='course_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.CourseSection', verbose_name='Ders Grubu'),
        ),
        migrations.AddField(
            model_name='sectionlettergrade',
            name='letter_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.LetterGrade', verbose_name='Harf Notu'),
        ),
        migrations.AddField(
            model_name='registrygrade',
            name='letter_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.SectionLetterGrade', verbose_name='Harf Notu'),
        ),
        migrations.AddField(
            model_name='registrygrade',
            name='section_registry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.SectionRegistry', verbose_name='Kayıt'),
        ),
        migrations.AddField(
            model_name='assignmentgrade',
            name='section_assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.SectionProcessAssignment', verbose_name='Grup Görevi'),
        ),
        migrations.AddField(
            model_name='assignmentgrade',
            name='section_registry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.SectionRegistry', verbose_name='Kayıt'),
        ),
    ]
