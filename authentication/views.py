from rest_framework.permissions import AllowAny
from .serializers import  CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Вью для логина с кастомным ответом
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = (AllowAny,)

class CustomTokenRefreshView(TokenRefreshView):
    """
    Вью для обновления токена
    """
    permission_classes = (AllowAny,)

