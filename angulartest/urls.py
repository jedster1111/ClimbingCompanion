"""
Definition of urls for ClimbingCompanion.
"""

from django.conf.urls import include, url
from angulartest.views import angularTest

urlpatterns = [
    url(r'^$', angularTest, name='angularTest')
]


                          

