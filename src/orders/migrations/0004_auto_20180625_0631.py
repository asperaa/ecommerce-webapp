# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-25 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20180625_0631'),
        ('orders', '0003_auto_20180624_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='addresses.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='addresses.Address'),
        ),
    ]
