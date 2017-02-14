from django.conf.urls import include, url
from logbook import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


#urlpatterns = [
#   url(r'^$', views.ClimbList.as_view()),
#   url(r'^(?P<pk>[0-9]+)/$', views.ClimbDetail.as_view()),
#   url(r'^users/$', views.UserList.as_view()),
#   url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#]
#
#urlpatterns = format_suffix_patterns(urlpatterns)
                          
schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
# /logbook/centres/
router.register(r'centres', views.CentreViewSet)
# /logbook/climbs/
router.register(r'climbs', views.ClimbViewSet)
# /logbook/users/
router.register(r'users', views.UserViewSet)


urlpatterns = [
        url('^schema/$', schema_view),
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ]
