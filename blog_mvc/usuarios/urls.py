from  django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Usuario_views

""" debes recordar que cuando estas tabajando con viewsets , las 
vistas se generan por default con django pero si hay que definirlas o algo asi """
router = DefaultRouter()
router.register(r'usuarios',Usuario_views)
urlpatterns= [
    path('usuarios/',include(router.urls))
]