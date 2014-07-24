from django.conf.urls import patterns, include, url

from django.contrib import admin
from existence_hashing import views
 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'improved_control.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^existence/', include('existence_hashing.urls')),
    url(r'^control/', include('existence_checking.urls')),
)
