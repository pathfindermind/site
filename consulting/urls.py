from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from feedback_app.views import ContactCreateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'consulting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/', include('feedback_app.urls')),
    url(r'^$', include('page.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
