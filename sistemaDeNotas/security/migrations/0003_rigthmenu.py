# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-16 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_auto_20180403_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='RigthMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('parent', models.BigIntegerField(null=True, verbose_name=10)),
                ('depth', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=255, null=True)),
                ('order', models.IntegerField(default=0)),
                ('text', models.CharField(default=b'', max_length=255)),
                ('url', models.CharField(default=b'', max_length=255)),
                ('type', models.CharField(max_length=255, null=True)),
                ('icon', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
