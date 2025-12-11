from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

from timeline.mixins import ActionLogMixin

class TaskViewSet(ActionLogMixin, viewsets.ModelViewSet):
    """
    Работа с задачами.
    CRUD операции.
    """

    queryset = Task.objects.all().select_related('assigned_to', 'deal', 'contact')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['status', 'assigned_to', 'deal', 'contact']
    
    search_fields = ['title', 'description']
    
    ordering_fields = ['due_date', 'created_at']
    ordering = ['due_date']