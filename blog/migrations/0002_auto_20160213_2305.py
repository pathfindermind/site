# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(verbose_name='\u0427\u041f\u0423')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='blogentry',
            options={'ordering': ('-published_at',), 'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u044c \u0431\u043b\u043e\u0433\u0430', 'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438 \u0431\u043b\u043e\u0433\u0430'},
        ),
        migrations.RemoveField(
            model_name='blogentry',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blogentry',
            name='date',
        ),
        migrations.AddField(
            model_name='blogentry',
            name='body',
            field=models.TextField(null=True, verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='\u0412 \u0447\u0435\u0440\u043d\u043e\u0432\u0438\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(upload_to=b'img/', verbose_name=b'Image', blank=True),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='slug',
            field=models.SlugField(default=1, verbose_name='\u0427\u041f\u0423'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogentry',
            name='tease',
            field=models.TextField(verbose_name='\u0422\u0438\u0437\u0435\u0440', blank=True),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='title',
            field=models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='category',
            field=models.ForeignKey(related_name='entries', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='blog.Category', null=True),
        ),
    ]
