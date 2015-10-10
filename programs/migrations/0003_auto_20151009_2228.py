# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20151009_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='courses',
            field=models.ManyToManyField(to='programs.Course', blank=True),
        ),
    ]
