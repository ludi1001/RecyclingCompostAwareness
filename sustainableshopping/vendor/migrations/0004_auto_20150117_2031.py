# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='desc',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='lat',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='lng',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
            preserve_default=True,
        ),
    ]
