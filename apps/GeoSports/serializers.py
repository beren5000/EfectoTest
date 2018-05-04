from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.GeoSports.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name')


class ProfileSerializer (serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = ('pk', 'user', 'nationality', 'gender', 'date_of_birth', 'created')
