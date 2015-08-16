# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20150816_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cover_used',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='resume_used',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='site_used',
            field=models.CharField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='updated',
            field=models.DateTimeField(verbose_name=b'updated', blank=True),
        ),
    ]
