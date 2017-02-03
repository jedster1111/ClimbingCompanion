# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0003_centre_climb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='climb',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='climb',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='climb',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climbs', to='logbook.Centre'),
        ),
    ]