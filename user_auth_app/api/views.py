from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from user_auth_app.models import UserProfile
from .serializers import RegisterSerializer, UserProfileSerializer


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Registrieren muss ohne Login gehen
