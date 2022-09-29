from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework import permissions


from hello.models import User, Ride, RideEvent
from hello.serializers import UserSerializer, RideSerializer, RideEventSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-first_name')
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('first_name', 'last_name', 'email', 'phone')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().order_by('-rider')
    serializer_class = RideSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('status')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all().order_by('-ride')
    serializer_class = RideEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



