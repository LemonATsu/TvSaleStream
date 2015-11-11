# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0004_product_ownername'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
