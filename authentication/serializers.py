from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Кастомный сериализатор для логина.
    Возвращает токены + информацию о пользователе (ID, имя, роль).
    """
    def validate(self, attrs):
        
        data = super().validate(attrs)

        
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['full_name'] = f"{self.user.first_name} {self.user.last_name}".strip()
        data['is_admin'] = self.user.is_staff  

        
        # { "access": "...", "refresh": "...", "user_id": 1, "is_admin": true }
        return data
    




