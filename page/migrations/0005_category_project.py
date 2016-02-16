# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name (Eng, \xd0\xb2 \xd0\xbd\xd0\xb8\xd0\xb6\xd0\xbd\xd0\xb5\xd0\xbc \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb5)')),
                ('slug', models.SlugField(verbose_name=b'Slug')),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb0 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8 \xd0\xb2 \xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c\xd1\x82\xd1\x80 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x80: .category1')),
                ('section', models.CharField(default=b'\xd0\x92\xd1\x81\xd0\xb5', max_length=255, verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e', choices=[('\u0412\u0441\u0435', b'\xd0\x92\xd1\x81\xd0\xb5'), ('\u0413\u0430\u0440\u0430\u043d\u0442\u0438\u0438', b'\xd0\x93\xd0\xb0\xd1\x80\xd0\xb0\xd0\xbd\xd1\x82\xd0\xb8\xd0\xb8'), ('IT - \u043a\u043e\u043d\u0441\u0430\u043b\u0442\u0438\u043d\u0433', b'IT - \xd0\xba\xd0\xbe\xd0\xbd\xd1\x81\xd0\xb0\xd0\xbb\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3'), ('\u041e\u0446\u0435\u043d\u043a\u0430', b'\xd0\x9e\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb0')])),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('image', models.ImageField(upload_to=b'img/', verbose_name=b'image', blank=True)),
                ('detail_url', models.CharField(max_length=255)),
                ('category', models.ForeignKey(related_name='project', to='page.Category')),
            ],
        ),
    ]
