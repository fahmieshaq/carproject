from rest_framework import serializers
from django.contrib.auth import get_user_model

""" HyperlinkedModelSerializer throws this error:
Could not resolve URL for hyperlinked relationship using view name "permission-detail". You may have 
failed to include the related model in your API, or incorrectly configured the `lookup_field` attribute on this field.

"""
class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
