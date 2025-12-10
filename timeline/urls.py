from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, ActionLogReadOnlyViewSet

app_name = 'timeline'

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'logs', ActionLogReadOnlyViewSet, basename='logs')

urlpatterns = [
    path('', include(router.urls)),
]