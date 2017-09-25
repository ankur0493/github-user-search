# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_usearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubuserdata',
            name='github_user_created',
            field=models.DateTimeField(null=True, verbose_name='User created datetime for Github'),
        ),
        migrations.AlterField(
            model_name='githubuserdata',
            name='github_user_updated',
            field=models.DateTimeField(null=True, verbose_name='User updated datetime for Github'),
        ),
    ]