from rest_framework import viewsets, filters
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserSerializer

from .permissions import IsAdminOrReadOnly 
from timeline.mixins import ActionLogMixin

class UserViewSet(ActionLogMixin, viewsets.ModelViewSet):
    """
    Работа с пользователями.
    CRUD операции.
    Обычным пользователям доступны только операции чтения.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    
    permission_classes = [IsAdminOrReadOnly]

    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    
    
    filterset_fields = ['is_staff', 'is_active']
    
    
    search_fields = ['username', 'first_name', 'last_name', 'email']
    
   
    ordering_fields = ['date_joined', 'username', 'last_name']