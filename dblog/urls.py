from django.conf.urls.defaults import patterns, include, url
from blog.rss import EntriesFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comment/', include('django.contrib.comments.urls')),
    url(r'^feed/', EntriesFeed()),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^([^/]+)$', 'blog.views.entry', name='entry'),
  )
