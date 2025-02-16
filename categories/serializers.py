from rest_framework import serializers
from .models import Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'user_id','name', 'created_at', 'updated_at']