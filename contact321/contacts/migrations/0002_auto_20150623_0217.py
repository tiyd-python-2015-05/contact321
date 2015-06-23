# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('kind', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('kind', models.CharField(blank=True, max_length=100)),
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
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='email',
            name='contact',
            field=models.ForeignKey(to='contacts.Contact'),
        ),
    ]
