# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442', 'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442', 'verbose_name_plural': '\u041f\u0440\u043e\u0435\u043a\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': '\u0421\u043b\u0430\u0439\u0434', 'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a', 'verbose_name_plural': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438'},
        ),
    ]
