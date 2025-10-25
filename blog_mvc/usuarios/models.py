from django.db import models


class Users_model(models.Model):

    username =  models.CharField(blank= False, null= False)
    email = models.EmailField(unique=True, blank=False, null= False)
    password = models.CharField(blank= False, null= False)
