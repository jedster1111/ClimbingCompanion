from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from logbook.serializers import *
from logbook.permissions import IsOwnerOrReadOnly

from .models import Coder, Climb, Centre

class ClimbViewSet(viewsets.ModelViewSet):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class CentreViewSet(viewsets.ModelViewSet):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    coder_list = Coder.objects.all()
    context = {'coder_list':coder_list,}
    return render(request,'logbook/index.html', context)