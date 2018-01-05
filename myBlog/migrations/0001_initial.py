# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, blank=True)),
                ('keyword', models.CharField(max_length=100, null=True, blank=True)),
                ('content', simditor.fields.RichTextField()),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('like', models.IntegerField(null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'articles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Life',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titlePage', models.ImageField(upload_to='live/')),
                ('title', models.TextField(null=True, blank=True)),
                ('keyword', models.CharField(max_length=100, null=True, blank=True)),
                ('content', simditor.fields.RichTextField()),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
