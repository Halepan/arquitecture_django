from django.test import TestCase
from usuarios.serializer import Usuario_serializer

class tesserializerusser(TestCase):
    """el testeo del serializador es muy parecido al de models se
      utiliza TestCase y el archivo que se pienza testear para validar el test"""
    
    def test_validacion_entrada(self):
        serializer = Usuario_serializer()
        self.assertIsNotNone(serializer)
