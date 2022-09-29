from django.contrib.auth import logout


from rest_framework import viewsets
from rest_framework import permissions


from hello.models import User, Ride, RideEvent
from hello.serializers import UserSerializer, RideSerializer, RideEventSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-first_name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def logout_view(request):
        logout(request)


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().order_by('-rider')
    serializer_class = RideSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def logout_view(request):
        logout(request)


class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all().order_by('-created_at')
    serializer_class = RideEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def logout_view(request):
        logout(request)