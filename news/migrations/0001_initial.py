# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 08:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('text_en', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 5, 5, 8, 25, 26, 801773, tzinfo=utc))),
            ],
        ),
    ]