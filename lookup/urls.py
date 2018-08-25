from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from lookup import views

app_name = 'lookup'

router = DefaultRouter()
router.register(r'urlinfo/v1', views.LookUpViewSet, 'lookup')
router.register(r'user', views.UserViewSet, 'user')

urlpatterns = [
    url(r'^', include(router.urls))
]
