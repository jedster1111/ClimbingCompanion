# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=40)),
                ('cool', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], help_text='Answer wisely', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Coders',
        ),
    ]
