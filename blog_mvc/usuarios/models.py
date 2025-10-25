from django.db import models
from django.contrib.auth.models import User

class Users_model(User):
    class Meta():
        username =  models.CharField(blank= False, null= False)
        email = models.EmailField(unique=True, blank=False, null= False)
        password = models.CharField(blank=False,null = False)
