from __future__ import absolute_import

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin; admin.autodiscover()
from django.contrib.comments.feeds import LatestCommentFeed
from .. import views
from ..aggregator.feeds import CommunityAggregatorFeed
from ..blog.feeds import WeblogEntryFeed

urlpatterns = patterns('',
    (r'^$', views.homepage),
    (r'^accounts/', include('django_website.accounts.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/$', views.comments),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^community/', include('django_website.aggregator.urls')),
    (r'^contact/', include('django_website.contact.urls')),
    (r'^r/', include('django.conf.urls.shortcut')),
    (r'^rss/weblog/$', WeblogEntryFeed()),
    (r'^rss/comments/$', LatestCommentFeed()),
    (r'^rss/community/$', CommunityAggregatorFeed()),
    (r'^sitemap\.xml$', views.sitemap),
    (r'^weblog/', include('django_website.blog.urls')),
    (r'', include('django_website.legacy.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )

# Add flatpages *after* media to avoid catching it.
urlpatterns += patterns('', (r'', include('django.contrib.flatpages.urls')))