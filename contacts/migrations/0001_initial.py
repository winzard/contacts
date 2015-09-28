# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_ymap.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('enabled', models.BooleanField(default=True, db_index=True, verbose_name='Enabled')),
                ('address', models.CharField(max_length=255, verbose_name='Address', db_index=True)),
                ('coords', django_ymap.fields.YmapCoord(db_index=True, max_length=255, null=True, verbose_name='Yandex Map Coordinates', blank=True)),
                ('phone', models.CharField(max_length=100, verbose_name='Main Phone Number', db_index=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Main Email', blank=True)),
                ('priority', models.IntegerField(default=0, help_text='From 10 to 1', verbose_name='Priority')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75, verbose_name='Email', db_index=True)),
                ('comment', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Comment', blank=True)),
                ('contact', models.ForeignKey(verbose_name='Contact', to='contacts.Contact')),
            ],
            options={
                'verbose_name': 'Emails',
                'verbose_name_plural': 'Email',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name', db_index=True)),
                ('link', models.CharField(max_length=255, verbose_name='Link', db_index=True)),
                ('comment', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Comment', blank=True)),
                ('contact', models.ForeignKey(verbose_name='Contact', to='contacts.Contact')),
            ],
            options={
                'verbose_name': 'Extra Links',
                'verbose_name_plural': 'Extra Link',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=100, verbose_name='Phone Number', db_index=True)),
                ('comment', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Comment', blank=True)),
                ('contact', models.ForeignKey(verbose_name='Contact', to='contacts.Contact')),
            ],
            options={
                'verbose_name': 'Phone Number',
                'verbose_name_plural': 'Phone Numbers',
            },
            bases=(models.Model,),
        ),
    ]
