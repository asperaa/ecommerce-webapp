# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-19 05:11
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cart',
            managers=[
                ('user', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
