from django.test import TestCase
from usuarios.models import UsersPersonalizado_model

class testusuario(TestCase):

    def test_create_user(self):
        #se crea una instancia en la cual no de se guarda en la base de datos pero si es funcionable para testear si funcionara
        userM = UsersPersonalizado_model.objects.create_user(username="henry",email = "alejandrohenry@gmail.com", password="henry12345678")

        self.assertEqual(userM.username, "henry")
        self.assertEqual(userM.email,"alejandrohenry@gmail.com")
        self.assertTrue(userM.check_password("henry12345678"))

    def test_have_email(self):
        #este test sirve para validar si creo un email en el usuario cuando se cree
        userM = UsersPersonalizado_model.objects.create_user(username="henry",email = "alejandrohenry@gmail.com", password="henry12345678")

        self.assertTrue(userM.email)
        self.assertFalse(userM.check_password("henry1234567"))

