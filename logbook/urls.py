from django.conf.urls import include, url
from logbook import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   url(r'^$', views.ClimbList.as_view()),
   url(r'^(?P<pk>[0-9]+)/$', views.ClimbDetail.as_view()),
   url(r'^users/$', views.UserList.as_view()),
   url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
                          

