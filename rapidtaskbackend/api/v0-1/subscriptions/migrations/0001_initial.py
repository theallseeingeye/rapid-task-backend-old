# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('subscribed', models.BooleanField(default=True)),
                ('notes', models.TextField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
