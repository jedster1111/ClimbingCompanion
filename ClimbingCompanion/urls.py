"""
Definition of urls for ClimbingCompanion.
"""

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from logbook.views import index


urlpatterns = [
    # Examples:
    # url(r'^$', ClimbingCompanion.views.home, name='home'),
    # url(r'^ClimbingCompanion/', include('ClimbingCompanion.ClimbingCompanion.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^angulartest/', include('angulartest.urls')),
    url(r'^$', index, name='index'),
]


                          

