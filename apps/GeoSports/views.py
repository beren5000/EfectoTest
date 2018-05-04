from django.shortcuts import render
from django.contrib.auth.models import User, Group
from apps.GeoSports.models import Profile
from rest_framework import viewsets
# Create your views here.
from apps.GeoSports.serializers import ProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Profiles to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
