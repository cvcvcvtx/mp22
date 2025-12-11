from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StageViewSet, DealViewSet

router = DefaultRouter()
router.register(r'stages', StageViewSet, basename = 'stages')
router.register(r'deals', DealViewSet, basename = 'deals')

urlpatterns = [
    path('', include(router.urls)),
]