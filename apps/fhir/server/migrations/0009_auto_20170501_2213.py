# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-01 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_supportedresourcetype_resourcetype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcerouter',
            name='fhir_path',
        ),
        migrations.AddField(
            model_name='resourcerouter',
            name='cert_file',
            field=models.TextField(blank=True, help_text='Name of Client Certificate file', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='resourcerouter',
            name='client_auth',
            field=models.BooleanField(default=False, help_text='Is Client Authentication Required?'),
        ),
        migrations.AddField(
            model_name='resourcerouter',
            name='fhir_url',
            field=models.URLField(default='http://localhost:8000/change_this_url', verbose_name='Full URL to FHIR API with terminating /'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcerouter',
            name='key_file',
            field=models.TextField(blank=True, help_text='Name of Client Key file', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='resourcerouter',
            name='name',
            field=models.CharField(default='change_this_name', max_length=254, verbose_name='Friendly Server Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcerouter',
            name='server_verify',
            field=models.BooleanField(default=False, help_text='Server Verify (Default=False)'),
        ),
        migrations.AddField(
            model_name='resourcerouter',
            name='shard_by',
            field=models.CharField(default='Patient', max_length=80, verbose_name='Key Resource type'),
        ),
    ]
