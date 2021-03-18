from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'added_by', 'name', 'description', 'category','created_at' )
        model = Animal