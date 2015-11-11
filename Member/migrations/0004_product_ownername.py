# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0003_product_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ownerName',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
