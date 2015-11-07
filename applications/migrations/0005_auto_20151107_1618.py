# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20150816_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='equity_high',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=5, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='equity_low',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=5, blank=True),
        ),
    ]
