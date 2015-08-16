# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20150816_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='notes',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
