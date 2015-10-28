# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20151028_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='difficulty',
            field=models.CharField(default=b'', max_length=1, null=True, choices=[(b'E', b'easy'), (b'M', b'medium'), (b'H', b'hard')]),
        ),
    ]
