from rest_framework import serializers
from .models import Issue

class IssueSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Issue
        fields = '__all__'
