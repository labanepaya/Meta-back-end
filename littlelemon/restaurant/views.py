from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for retrieving the User object created by createsuperuser.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import generics
from .models import MenuTable
from .serializers import MenuTableSerializer


class MenuItemView(generics.ListCreateAPIView):
    """
    API view for listing and creating menu items.
    """

    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating and deleting a single menu item.
    """

    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer

