# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-25 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth','0008_alter_user_username_max_length'),
        ('security', '0006_leftmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='leftmenu',
            name='perm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Permission', verbose_name=b'Permission'),
        ),
    ]