from django.conf.urls import include, url
from logbook import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   url(r'^$', views.climb_list),
   url(r'^(?P<pk>[0-9]+)/$', views.climb_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
                          

