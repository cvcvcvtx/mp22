from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    правило:
    - Чтение (GET, HEAD, OPTIONS) разрешено всем авторизованным пользователям.
    - Изменение и удаление (POST, PUT, PATCH, DELETE) - только администраторам.
    """
    def has_permission(self, request, view):
        
        if not request.user.is_authenticated:
            return False

        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        
        return request.user.is_staff