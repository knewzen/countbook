# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operations',
            new_name='Operation',
        ),
        migrations.RenameModel(
            old_name='Records',
            new_name='Record',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='operation',
            new_name='operation_id',
        ),
    ]
