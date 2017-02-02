from django.conf.urls import include, url
from logbook import views

urlpatterns = [
   url(r'^$', views.climb_list),
   url(r'^(?P<pk>[0-9]+)/$', views.climb_detail),
]


                          

