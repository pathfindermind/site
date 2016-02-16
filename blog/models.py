# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(u'Название', max_length=50)
    slug = models.SlugField(u'ЧПУ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'категорию'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return u'%s' % self.name


class EntryManager(models.Manager):

    def published(self):
        return self.filter(draft=False)

    def drafted(self):
        return self.filter(draft=True)


class BlogEntry(models.Model):

    title = models.CharField(u'Заголовок', max_length=50)
    slug = models.SlugField(u'ЧПУ')
    image = models.ImageField('Image', upload_to='img/', blank=True)
    tease = models.TextField(u'Тизер', blank=True)
    body = models.TextField(u'Контент')
    draft = models.BooleanField(u'В черновики', default=True)
    created_at = models.DateTimeField(u'Дата создания', default=datetime.now)
    published_at = models.DateTimeField(u'Дата публикации', default=datetime.now)
    category = models.ForeignKey(Category, related_name='entries', verbose_name = "Категория")

    objects = EntryManager()

    class Meta:
        verbose_name = u'запись блога'
        verbose_name_plural = u'Записи блога'
        ordering = ('-published_at',)

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_details', (), {'year': self.published_at.year,
                                     'month': self.published_at.strftime('%m'),
                                     'day': self.published_at.strftime('%d'),
                                     'slug': self.slug})
