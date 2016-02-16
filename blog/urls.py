from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    # indexes
    url(r'^$', 'index', name='blog_index'),
    url(r'^category/(?P<id>\d+)-(?P<slug>[-\w]+)/$', 'category', name='blog_category'),

    # archives
    url(r'^archive/(?P<year>\d{4})/$', 'archive_year', name='blog_archive_year'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month', name='blog_archive_month'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive_day', name='blog_archive_day'),

    # details
    url(r'^details/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'details', name='blog_details'),
)
