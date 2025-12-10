from rest_framework import serializers
from .models import Stage, Deal
from contacts.models import Contact
from django.contrib.auth import get_user_model

User = get_user_model()

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class DealSerializer(serializers.ModelSerializer):
    contact_name = serializers.CharField(source='contact.first_name', read_only=True)
    stage_name = serializers.CharField(source='stage.name', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.username', read_only=True)

    class Meta:
        model = Deal
        fields = [
            'id', 
            'title', 
            'contact', 'contact_name',  
            'assigned_to', 'assigned_to_name',
            'stage', 'stage_name',
            'value', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']