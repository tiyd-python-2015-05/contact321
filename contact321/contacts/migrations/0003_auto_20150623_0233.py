# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20150623_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='contact',
            field=models.ForeignKey(related_name='emails', to='contacts.Contact'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(related_name='phones', to='contacts.Contact'),
        ),
    ]
