# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-30 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0002_auto_20190125_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_model',
            name='contact_no',
            field=models.IntegerField(null=True),
        ),
    ]