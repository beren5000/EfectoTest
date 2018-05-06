from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.GeoSports.models import Profile, CounterCountries


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name')


class ProfileSerializer (serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = ('pk', 'user', 'nationality', 'gender', 'date_of_birth', 'created')


class ProfilesByCountrySerializer(serializers.Serializer):
    nationality = serializers.CharField(max_length=256)
    count = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return CounterCountries(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
