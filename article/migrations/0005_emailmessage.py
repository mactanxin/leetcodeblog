# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20151020_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(null=True, blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('ip_address', models.GenericIPAddressField()),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
