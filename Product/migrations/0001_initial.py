# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=10, decimal_places=0)),
                ('owner', models.DecimalField(max_digits=10, decimal_places=0)),
                ('live', models.DecimalField(default=0, max_digits=2, decimal_places=0)),
                ('ownerName', models.CharField(max_length=20)),
            ],
        ),
    ]
