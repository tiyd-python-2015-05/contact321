# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('kind', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phone', models.CharField(max_length=20)),
                ('kind', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(related_name='phones', to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='email',
            name='contact',
            field=models.ForeignKey(related_name='contacts', to='contacts.Contact'),
        ),
    ]
