from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.CharField(source='assigned_to.username', read_only=True)
    deal_title = serializers.CharField(source='deal.title', read_only=True)
    contact_name = serializers.CharField(source='contact.first_name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 
            'title', 
            'description', 
            'due_date', 
            'status',
            'assigned_to', 'assigned_to_name',  
            'deal', 'deal_title',              
            'contact', 'contact_name',         
            'created_at'
        ]