from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Stage, Deal
from .serializers import StageSerializer, DealSerializer

from timeline.mixins import ActionLogMixin

class StageViewSet(ActionLogMixin, viewsets.ModelViewSet):

    queryset = Stage.objects.all().order_by('order') 
    serializer_class = StageSerializer
    permission_classes = [permissions.IsAuthenticated] 


class DealViewSet(ActionLogMixin, viewsets.ModelViewSet):
    """
    Работа со сделками.
    CRUD операции.
    """

    queryset = Deal.objects.all().select_related('contact', 'stage', 'assigned_to') 
    serializer_class = DealSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['stage', 'contact', 'assigned_to']
    
    search_fields = ['title', 'contact__first_name', 'contact__last_name']
    
    ordering_fields = ['value', 'created_at', 'updated_at']
    ordering = ['-created_at'] 

    def perform_create(self, serializer):

        serializer.save()
        self._log_action('CREATED', serializer.instance)