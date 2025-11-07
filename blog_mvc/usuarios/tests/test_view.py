from django.test import TestCase
from usuarios.views import Usuario_views

class testviewsusers(TestCase):
    def setUp(self):
        return super().setUp()

    def test_views_exsit(self):

        view = Usuario_views()
        self.assertIsNotNone(view)
        print("La vista existe")