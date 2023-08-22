from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Dronlar


class DronlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dronlar
        fields = '__all__'  # Tüm model alanlarını kullan


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'