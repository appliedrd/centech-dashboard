from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'centech2.views.home', name='home'),
    url(r'^centech/', include('tablebord.urls')),
    #url(r'^centech/', include('tablebord.urls', namespace="tablebord")),
    url(r'^admin/', include(admin.site.urls)),
)
