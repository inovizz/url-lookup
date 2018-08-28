"""Urls file for lookup app."""

from django.urls import re_path
from lookup import views

app_name = 'lookup'

urlpatterns = [
    re_path(
        r'^urlinfo/v1/(?P<domain>http[s]?:\/\/[\w$-*@.&+!(\),?:%]+)/'
        r'(?P<path>[\w\/$-*@.&+!(\),?:%"\'=]+)/$',
        views.url_lookup, name='url'),
    re_path(
        r'^urlinfo/v1/(?P<domain>http[s]?:\/\/[\w$-*_@.&+!(\),?:%]+)/$',
        views.url_lookup, name='url'),
    re_path(r'^urlinfo/v1/$', views.url_lookup, name='url')
]
