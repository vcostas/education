# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-27 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0007_leftmenu_perm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leftmenu',
            name='type',
        ),
        migrations.AddField(
            model_name='leftmenu',
            name='codename',
            field=models.CharField(default='defCode_', max_length=30, unique=True),
        ),
    ]
