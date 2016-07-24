
from django.conf.urls import patterns, url

from .api import PostListAPI

urlpatterns = [
    url(r'^api/posts/?$', PostListAPI.as_view(), name='post_list'),
]
