from django.conf.urls import patterns, url

from existence_hashing import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^generate/$',views.generate, name='generate'),
    url(r'^generate/(?P<country>\S+)/$',views.generate_for_country, name='generate_for_country'),
)
