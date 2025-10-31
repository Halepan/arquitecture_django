from rest_framework import viewsets
from .models import UsersPersonalizado_model
from .serializer import Usuario_serializer


class Usuario_views(viewsets.ModelViewSet):
    queryset = UsersPersonalizado_model.objects.all()
    serializer_class = Usuario_serializer
# Create your views here.
