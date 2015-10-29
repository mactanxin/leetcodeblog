#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(default='', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='difficulty',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'E', b'easy'), (b'M', b'medium'), (b'H', b'hard')]),
        ),
    ]
