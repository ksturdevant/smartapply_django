# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name=b'date created')),
                ('title', models.CharField(max_length=200)),
                ('salary_low', models.IntegerField()),
                ('salary_high', models.IntegerField()),
                ('equity_low', models.DecimalField(max_digits=9, decimal_places=5)),
                ('equity_high', models.DecimalField(max_digits=9, decimal_places=5)),
                ('site_used', models.CharField(max_length=400)),
                ('cover_used', models.CharField(max_length=100)),
                ('resume_used', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=1000)),
                ('updated', models.DateTimeField(verbose_name=b'updated')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated', models.DateTimeField(verbose_name=b'status updated')),
                ('status', models.CharField(max_length=50)),
                ('unique_ID', models.ForeignKey(to='applications.Application')),
            ],
        ),
    ]
