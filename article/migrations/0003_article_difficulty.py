# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_leedindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='difficulty',
            field=models.CharField(max_length=1, null=True, choices=[(b'E', b'easy'), (b'M', b'medium'), (b'H', b'hard')]),
        ),
    ]
