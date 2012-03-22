from django.conf.urls.defaults import patterns, include, url
import settings
import oembed
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
oembed.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'd_portfolio.views.show_tag', {'tag_title': 'home'}),
    
    url(r'^medium/(\w+)/$', 'd_portfolio.views.show_tag'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
        
    # url(r'^d_portfolio/', include('d_portfolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
