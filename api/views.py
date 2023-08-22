from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.models import Dronlar
from api.serializers import UserSerializer, GroupSerializer, DronlarSerializer


class DronViewSet(viewsets.ModelViewSet):
    queryset = Dronlar.objects.all()
    serializer_class = DronlarSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
