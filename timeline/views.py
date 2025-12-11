from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Activity, ActionLog
from .serializers import ActivitySerializer, ActionLogSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    """
    Работа с активностями.
    CRUD операции.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['contact', 'deal', 'type']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ActionLogReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Просмотр истории действий. 
    """
    queryset = ActionLog.objects.all()
    serializer_class = ActionLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.OrderingFilter]
    ordering = ['-timestamp']