from django.conf.urls import patterns, url

from tablebord import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /centech/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
# ex: /centech/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
# ex: /centech/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)