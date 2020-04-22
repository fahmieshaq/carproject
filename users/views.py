from rest_framework import viewsets
from django.contrib.auth import get_user_model
from . import serializers


class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.CustomUserModelSerializer
