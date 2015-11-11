# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=200)),
                ('online', models.DecimalField(max_digits=2, decimal_places=0)),
            ],
        ),
    ]
