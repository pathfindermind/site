# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160213_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='body',
            field=models.TextField(default=1, verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='category',
            field=models.ForeignKey(related_name='entries', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='blog.Category'),
        ),
    ]
