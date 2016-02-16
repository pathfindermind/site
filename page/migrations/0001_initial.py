# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('after_title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to=b'img/', verbose_name=b'image', blank=True)),
                ('detail_url', models.CharField(max_length=255)),
            ],
        ),
    ]
