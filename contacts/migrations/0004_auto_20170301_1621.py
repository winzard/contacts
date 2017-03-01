# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name', db_index=True)),
                ('priority', models.IntegerField(default=0, help_text='From 10 to 1', verbose_name='Priority')),
                ('contacts', models.ManyToManyField(to='contacts.Contact', verbose_name='Contacts')),
            ],
            options={
                'ordering': ('-priority',),
                'verbose_name': 'Contact Group',
                'verbose_name_plural': 'Contact Groups',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-priority',), 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]
