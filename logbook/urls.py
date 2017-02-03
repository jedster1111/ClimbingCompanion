from django.conf.urls import include, url
from logbook import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


#urlpatterns = [
#   url(r'^$', views.ClimbList.as_view()),
#   url(r'^(?P<pk>[0-9]+)/$', views.ClimbDetail.as_view()),
#   url(r'^users/$', views.UserList.as_view()),
#   url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#]
#
#urlpatterns = format_suffix_patterns(urlpatterns)
                          
router = DefaultRouter()
# /logbook/climbs/
router.register(r'climbs', views.ClimbViewSet)
# /logbook/users/
router.register(r'users', views.UserViewSet)

urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
