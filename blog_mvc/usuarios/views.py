from rest_framework import viewsets
from .models import UsersPersonalizado_model
from .serializer import Usuario_serializer


class User_views(viewsets.ModelViewSet):
    queryset = UsersPersonalizado_model
    serializer_class = Usuario_serializer
    def detall():
        pass

    def list():
        pass
# Create your views here.
