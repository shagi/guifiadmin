# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guifi', '0001_initial'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Person', verbose_name='person')),
            ],
            options={
                'verbose_name': 'maintainer',
                'verbose_name_plural': 'maintainer',
            },
        ),
        migrations.CreateModel(
            name='NodeMaintainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintainers.Maintainer', verbose_name='maintainer')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guifi.Node', verbose_name='node')),
            ],
            options={
                'verbose_name': 'node maintainer',
                'verbose_name_plural': 'none maintainers',
            },
        ),
        migrations.CreateModel(
            name='ZoneMaintainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintainers.Maintainer', verbose_name='maintainer')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guifi.Zone', verbose_name='zone')),
            ],
            options={
                'verbose_name': 'zone maintainer',
                'verbose_name_plural': 'zone maintainers',
            },
        ),
    ]