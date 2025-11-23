from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Кастомный сериализатор для логина.
    Возвращает токены + информацию о пользователе (ID, имя, роль).
    """
    def validate(self, attrs):
        # Получаем стандартные токены (access и refresh)
        data = super().validate(attrs)

        # self.user - это пользователь, который прошел аутентификацию
        # Добавляем дополнительные поля в ответ JSON
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['full_name'] = f"{self.user.first_name} {self.user.last_name}".strip()
        data['is_admin'] = self.user.is_staff  # Флаг админа/менеджера

        # Теперь React получит: 
        # { "access": "...", "refresh": "...", "user_id": 1, "is_admin": true }
        return data
    


# ... (твой предыдущий CustomTokenObtainPairSerializer) ...

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'},
        min_length=8 # Минимальная длина пароля
    )
    
    # Добавляем подтверждение пароля (опционально, но полезно)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # Поля, которые мы требуем при регистрации
        fields = ('username', 'password', 'password_confirm', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        # Проверка, что пароли совпадают
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

    def create(self, validated_data):
        # Удаляем password_confirm, так как его нет в модели User
        validated_data.pop('password_confirm')
        
        # КРИТИЧЕСКИЙ МОМЕНТ:
        # Мы используем User.objects.create_user(), а не create().
        # create_user() берет на себя хеширование пароля.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user