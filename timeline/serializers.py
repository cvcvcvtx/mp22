from rest_framework import serializers
from .models import Activity, ActionLog

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'read_only': True} 
        }

class ActionLogSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения логов """
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ActionLog
        fields = '__all__'