
from django.conf.urls import patterns, url

from .api import PostListAPI, TestTagListAPI

urlpatterns = [
    url(r'^api/posts/?$', PostListAPI.as_view(), name='blog_api_post_list'),
    url(r'^api/testtags/?$', TestTagListAPI.as_view(), name='blog_api_test_tags_list')
]
