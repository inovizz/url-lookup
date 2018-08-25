"""Serializer class for LookUps and User."""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import LookUp


class LookUpSerializer(serializers.ModelSerializer):
    """Serializer class for LookUp model."""
    class Meta:
        """Meta class for LookUpSerializer."""
        model = LookUp
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for User model."""
    class Meta:
        """Meta class for UserSerializer."""
        model = User
        fields = '__all__'
