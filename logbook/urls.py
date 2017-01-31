"""
Definition of urls for ClimbingCompanion.
"""

from django.conf.urls import include, url
#import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', ClimbingCompanion.views.home, name='home'),
    # url(r'^ClimbingCompanion/', include('ClimbingCompanion.ClimbingCompanion.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR+'/core/static/', 'show_indexes': True}),
]


                          

