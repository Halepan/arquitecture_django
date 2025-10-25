from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersPersonalizado_model(AbstractUser):

    email = models.EmailField(unique=True, blank=False, null= False,primary_key=True)

    class Meta:
        db_table='UsersPersonalizado_model'
