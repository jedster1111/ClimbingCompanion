from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()
from logbook.views import index


urlpatterns = [
    # Examples:
    # url(r'^$', ClimbingCompanion.views.home, name='home'),
    # url(r'^ClimbingCompanion/', include('ClimbingCompanion.ClimbingCompanion.urls')),
    url('', include('django.contrib.auth.urls')),
    url('/logout/$', auth_views.logout,{'LOGOUT_REDIRECT_URL':'/'}),
]



                          

