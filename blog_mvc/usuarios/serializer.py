from rest_framework import serializers
from .models import UsersPersonalizado_model

class Usuario_serializer(serializers.ModelSerializer):
    class Meta():
        model = UsersPersonalizado_model
        fields = '__all__'