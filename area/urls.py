
from django.conf.urls import patterns, url

from .api import CityListAPI

urlpatterns = patterns('',
    url(r'^api/city/list/(?P<province>\d+)$', CityListAPI.as_view(), name='city_list'),
)
