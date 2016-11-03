# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('invoice_number', models.CharField(max_length=50, verbose_name='invoice number')),
                ('total', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='total')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='providers_invoices', to='accounting.Person', verbose_name='provider')),
            ],
            options={
                'verbose_name': 'invoice',
                'verbose_name_plural': 'invoices',
            },
        ),
    ]