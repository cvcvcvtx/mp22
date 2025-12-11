from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers



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
    




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'},
        min_length=8 
    )
    
    
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        
        fields = ('username', 'password', 'password_confirm', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

    def create(self, validated_data):
        
        validated_data.pop('password_confirm')
        
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user