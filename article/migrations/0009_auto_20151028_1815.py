# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20151028_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='leedindex',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
