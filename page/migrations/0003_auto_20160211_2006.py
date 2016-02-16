# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20160210_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='after_title',
            field=models.CharField(max_length=255, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='detail_url',
            field=models.CharField(max_length=255, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0434\u0435\u0442\u0430\u043b\u044c\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='text',
            field=models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
    ]
