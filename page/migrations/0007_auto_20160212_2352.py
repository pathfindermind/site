# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20160212_2348'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='Worker',
        ),
    ]
