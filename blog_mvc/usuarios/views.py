from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .models import UsersPersonalizado_model
from .serializer import Usuario_serializer


class Usuario_views(viewsets.ModelViewSet):
    queryset = UsersPersonalizado_model.objects.all()
    serializer_class = Usuario_serializer

    def get_permissions(self):
        """aqui en modelviewset los permisos se gestionana de otra manera estos deben 
        ocurrir mediante el metod get permisos asignandole los pemisos a cada metodo"""

        if self.action in ['list','destroy']:#solo los administradores pueden listar todos los usuarios y eliminarlos 
            return IsAdminUser

        if self.action == 'create':#Cualquiera puede registrarst
            return AllowAny

        if self.action in ['retirve','update','partial_update']:#se requiere estar autenticado para poder ver un usuario y modificarlo 
            return IsAuthenticated


        return super().get_permissions()

