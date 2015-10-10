# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='course',
        ),
        migrations.AddField(
            model_name='instructor',
            name='courses',
            field=models.ManyToManyField(to='programs.Course'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='institution',
            field=models.ForeignKey(default='1', to='programs.Institution'),
            preserve_default=False,
        ),
    ]
