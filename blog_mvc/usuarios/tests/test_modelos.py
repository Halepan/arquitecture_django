from django.test import TestCase
from usuarios.models import Users_model

class testusuario(TestCase):

    def test_create_user(self):
        #se crea una instancia en la cual no de se guarda en la base de datos pero si es funcionable para testear si funcionara
        userM = Users_model.objects.create(username="henry",email = "alejandrohenry@gmail.com", password="henry12345678")

        self.assertEqual(userM.username, "henry")
        self.assertEqual(userM.email,"alejandrohenry@gamil.com")
        self.assertEqual(userM.password, "henry12345678")

    def test_have_email(self):
        #este test sirve para validar si genero un email en el usuario cuando se cree
        userM = Users_model.objects.create(username="henry",email = "alejandrohenry@gmail.com", password="henry12345678")

        self.assertTrue(userM.email)

        """reestructura y vuelve a hacer el models para que funcione como un usuario normal"""