from rest_framework import serializers

from hello.models import Ride, User, RideEvent


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', "role"]


class RideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ride
        fields = ['status', 'rider', 'from_location', 'to_location']


class RideEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RideEvent
        fields = ['ride', 'description', 'created_at']



