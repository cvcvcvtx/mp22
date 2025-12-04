from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с контактами.
    Автоматически создает CRUD: список, просмотр, создание, изменение, удаление.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter 
    ]
    
    # /?company=Google&assigned_to=1
    filterset_fields = ['company', 'assigned_to']    # фильтры (можно че то добавить, но не вижу смысла)

    # /?search=Иван
    search_fields = ['first_name', 'last_name', 'email', 'company', 'phone'] # поиск

    # /?ordering=-created_at (сначала новые)
    ordering_fields = ['created_at', 'last_name', 'first_name', 'company'] # сортировка
    
    ordering = ['-created_at']

    def perform_create(self, serializer):
       
        # если у контакта не указан ответственный менеджер то им становится тот кто сделал запрос
        if not serializer.validated_data.get('assigned_to'):
            serializer.save(assigned_to=self.request.user)
        else:
            serializer.save()


