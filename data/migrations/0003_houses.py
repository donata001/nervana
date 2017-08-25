# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150826_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(null=True)),
                ('region', models.CharField(max_length=5, null=True)),
                ('weight', models.FloatField(null=True)),
                ('bedrooms', models.IntegerField(null=True)),
                ('built_year', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
                ('vacancy', models.IntegerField(null=True)),
                ('nunit', models.IntegerField(null=True)),
                ('rooms', models.IntegerField(null=True)),
                ('utility', models.FloatField(null=True)),
                ('type', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
