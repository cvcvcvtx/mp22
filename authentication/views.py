# authentication/views.py
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Вью для логина с кастомным ответом
    """
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    """
    Эндпоинт для регистрации новых пользователей.
    """
    queryset = User.objects.all()
    #permission_classes = (AllowAny,) 
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer