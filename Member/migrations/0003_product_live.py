# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='live',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=0),
        ),
    ]
