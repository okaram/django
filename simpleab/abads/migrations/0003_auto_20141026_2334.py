# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abads', '0002_experimentad_experiment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experimentad',
            old_name='url',
            new_name='src_url',
        ),
        migrations.AddField(
            model_name='abexperiment',
            name='action_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
