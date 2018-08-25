from django.contrib.auth.models import User
from lookup.serializers import UserSerializer, LookUpSerializer
from rest_framework import viewsets
from .models import LookUp


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LookUpViewSet(viewsets.ModelViewSet):
    """
    LookUp view set to create, retrieve, update and delete the lookup
    object.
    """
    queryset = LookUp.objects.all()
    serializer_class = LookUpSerializer
