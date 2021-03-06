from __future__ import absolute_import

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.comments.feeds import LatestCommentFeed
from django.contrib.comments.models import Comment
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page
from ..aggregator.feeds import CommunityAggregatorFeed
from ..aggregator.models import FeedItem
from ..blog.feeds import WeblogEntryFeed
from ..sitemaps import FlatPageSitemap, WeblogSitemap

comments_info_dict = {
    'queryset': Comment.objects.filter(is_public=True).order_by('-submit_date'),
    'paginate_by': 15,
}

sitemaps = {
    'weblog': WeblogSitemap,
    'flatpages': FlatPageSitemap,
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'homepage.html'}, name="homepage"),
    (r'^accounts/', include('django_website.accounts.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^comments/$', 'django.views.generic.list_detail.object_list', comments_info_dict),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^community/add/(?P<feed_type_slug>[-\w]+)/',
         'django_website.aggregator.views.add_feed',
          name='community-add-feed'),
    url(r'^community/(?P<feed_type_slug>[-\w]+)/',
         'django_website.aggregator.views.feed_list',
          name="community-feed-list"),
    url(r'^community/', 'django_website.aggregator.views.index', name='community-index'),
    url(r'^contact/', include('django_website.contact.urls')),
    url(r'^r/', include('django.conf.urls.shortcut')),

    url(r'^rss/weblog/$', WeblogEntryFeed(), name='weblog-feed'),
    url(r'^rss/comments/$', LatestCommentFeed(), name='comments-feed'),
    url(r'^rss/community/$', CommunityAggregatorFeed(), name='aggregator-firehose-feed'),
    url(r'^rss/community/(?P<slug>[\w-]+)/$', CommunityAggregatorFeed(), name='aggregator-feed'),

    url(r'^sitemap\.xml$', cache_page(sitemap_views.sitemap, 60 * 60 * 6), {'sitemaps': sitemaps}),
    url(r'^weblog/', include('django_website.blog.urls')),
    url(r'^freenode\.9xJY7YIUWtwn\.html$', 'django.views.generic.simple.direct_to_template', {'template': 'freenode_tmp.html'}),
    url(r'^download$', 'django.contrib.flatpages.views.flatpage', {'url': 'download'}, name="download"),
    url(r'', include('django_website.legacy.urls')),
)

if not settings.PRODUCTION:
    urlpatterns += patterns("django.views",
        url(r"^media/(?P<path>.*)", "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        }),
    )

urlpatterns += patterns('',
    # flatpages need to be last b/c they match anything
    (r'', include('django.contrib.flatpages.urls')),
)

admin.autodiscover()
