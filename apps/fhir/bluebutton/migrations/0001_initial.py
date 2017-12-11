# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-16 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('server', '0017_resourcerouter_wait_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crosswalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fhir_id', models.CharField(blank=True, default='', max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user_id_type', models.CharField(choices=[('H', 'HICN'), ('M', 'MBI'), ('S', 'SSN')], default='H', max_length=1)),
                ('user_id_hash', models.CharField(blank=True, default='', max_length=64, verbose_name='PBKDF2 of User ID')),
                ('fhir_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.ResourceRouter')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
