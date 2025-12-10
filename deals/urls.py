from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StageViewSet, DealViewSet

router = DefaultRouter()
router.register(r'', StageViewSet)
router.register(r'', DealViewSet)

urlpatterns = [
    path('', include(router.urls)),
]