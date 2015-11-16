# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='comment',
            field=models.TextField(max_length=800, null=True, verbose_name='Comment', blank=True),
            preserve_default=True,
        ),
    ]
