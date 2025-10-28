from rest_framework import serializers
from .models import UsersPersonalizado_model

class Usuario_serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # Cambia a True
    
    class Meta:
        model = UsersPersonalizado_model
        fields = ['username','email','password']
    
    def create(self, validated_data):
        # 🔥 1 línea que soluciona todo
        return UsersPersonalizado_model.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # 🔥 1 línea que soluciona todo
        instance.save()
        return instance
