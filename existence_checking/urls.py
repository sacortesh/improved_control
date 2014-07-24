from django.conf.urls import patterns, url

from existence_checking import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^check/(?P<country>\S+)/(?P<passport>\S+)/$',views.check, name='check'),
)
