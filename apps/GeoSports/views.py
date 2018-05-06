from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action

from apps.GeoSports.models import Profile, NATIONALITY_OPTIONS
from rest_framework import viewsets, generics
from rest_framework.response import Response
# Create your views here.
from apps.GeoSports.serializers import ProfileSerializer, UserSerializer, ProfilesByCountrySerializer
from apps.GeoSports.models import CounterCountries


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

    serializer_class = ProfileSerializer

    @action(methods=['post'], detail=True, url_path='(\w{0,50})', url_name='filter')
    def get_queryset(self):
        country = self.request.query_params.get('country', None)
        gender = self.request.query_params.get('gender', None)
        birthdate = self.request.query_params.get('birthdate', None)
        queryset = Profile.objects.all()
        if country is not None:
            queryset = queryset.filter(nationality=country)
        if gender is not None:
            queryset = queryset.filter(gender=gender)
        if birthdate is not None:
            queryset = queryset.filter(date_of_birth=birthdate)
        return queryset


class ProfileByNationalityCount(viewsets.ViewSet):
    serializer_class = ProfilesByCountrySerializer
    queryset = User.objects.all()

    def list(self, request):
        resp = {}
        element_counter = 1
        for i in NATIONALITY_OPTIONS:
            count = Profile.objects.filter(nationality=i[0]).count()
            counter_country = CounterCountries(nationality=i[0], count=count)
            resp.update({i: counter_country})
            element_counter += 1
        serializer = ProfilesByCountrySerializer(instance=resp.values(), many=True)
        return Response(serializer.data)
