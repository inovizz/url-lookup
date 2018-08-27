from lookup import views
from django.urls import re_path

app_name = 'lookup'

urlpatterns = [
    re_path(
        r'^urlinfo/v1/(?P<domain>http[s]?:\/\/[\w$-*_@.&+!(\),?:%]+)/'
        r'(?P<path>[\w\/$-*_@.&+!(\),?:%"\'=]+)/$',
        views.url_lookup, name='url'),
    re_path(
        r'^urlinfo/v1/(?P<domain>http[s]?:\/\/[\w$-*_@.&+!(\),?:%]+)/$',
        views.url_lookup, name='url'),
    re_path(r'^urlinfo/v1/$', views.url_lookup, name='url')
]
