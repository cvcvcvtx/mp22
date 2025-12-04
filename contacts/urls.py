from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

app_name = 'contacts'


router = DefaultRouter()
router.register(r'', ContactViewSet, basename='contacts')

urlpatterns = [
    
    # GET /api/v1/contacts/ - список
    # POST /api/v1/contacts/ - создать
    # GET /api/v1/contacts/{id}/ - карточка
    # PUT /api/v1/contacts/{id}/ - изменить
    path('', include(router.urls)),
]