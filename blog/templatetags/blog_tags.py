# -*- coding: utf-8 -*-
from django import template
from blog.models import BlogEntry

register = template.Library()


@register.inclusion_tag('blog/titles.html')
def blog_title(blog):
    entries = BlogEntry.objects.all().order_by('-created_at')[:3]
    return {
        'entries': entries
    }