# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-03 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('relationship', models.CharField(max_length=64, verbose_name=b'Parentesco')),
                ('start_date', models.DateField(verbose_name=b'Fecha inicio vigencia')),
                ('end_date', models.DateField(null=True, verbose_name=b'Fecha fin vigencia')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.Student', verbose_name=b'Estudiante')),
            ],
            options={
                'verbose_name': 'Relacion responsable alumno',
                'verbose_name_plural': 'Relacion responsables alumno',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=64, verbose_name=b'Primer nombre')),
                ('second_name', models.CharField(blank=True, max_length=64, null=True, verbose_name=b'Segundo nombre')),
                ('last_name', models.CharField(max_length=64, verbose_name=b'Apellido')),
                ('identifier', models.CharField(max_length=64, verbose_name=b'identifier')),
                ('gender', models.CharField(max_length=1, null=True, verbose_name=b'gender')),
            ],
            options={
                'verbose_name': 'Responsable Alumno',
                'verbose_name_plural': 'Responsables Alumnos',
            },
        ),
        migrations.AddField(
            model_name='studenttutor',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.Tutor', verbose_name=b'Tutor'),
        ),
    ]
