# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=None),
            preserve_default=False,
        ),
    ]
