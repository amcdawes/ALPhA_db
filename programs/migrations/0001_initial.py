# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('level', models.CharField(default='FS', choices=[('FS', 'First term or sophomore'), ('INT', 'Intermediate methods'), ('EL', 'Elective lab courses'), ('ADV', 'Advanced Lab')], max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GradRate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('USNewsRank', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('course', models.ForeignKey(to='programs.Course')),
            ],
        ),
        migrations.AddField(
            model_name='gradrate',
            name='institution',
            field=models.ForeignKey(to='programs.Institution'),
        ),
        migrations.AddField(
            model_name='course',
            name='institution',
            field=models.ForeignKey(to='programs.Institution'),
        ),
    ]
