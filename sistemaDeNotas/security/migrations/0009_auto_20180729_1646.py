# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-29 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0008_auto_20180727_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': (('view_birthday', 'Ver cumplea\xf1os'),), 'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
    ]