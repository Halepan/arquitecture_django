# users/tests/test_serializers.py
from django.test import TestCase
from usuarios.models import UsersPersonalizado_model as User
from usuarios.serializer import Usuario_serializer as User_serializer

class TestUserSerializer(TestCase):
    """
    Tests completos para el UserSerializer
    Seguimos el enfoque TDD: Tests primero, código después
    """
    
    def setUp(self):
        """Datos comunes para los tests"""
        self.valid_user_data = {
            'username': 'testuser',
            'email': 'test@ejemplo.com',
            'password': 'testpass123'
        }
    
    # ✅ TEST 1: Existencia del serializador
    def test_serializador_existe(self):
        """Verificar que el serializador se puede importar y crear"""
        serializer = User_serializer()
        self.assertIsNotNone(serializer)
        print("✅ ¡Serializador existe!")
    
    # ✅ TEST 2: Serialización (User → JSON)
    def test_serializacion_user_a_json(self):
        """Verificar que un User se convierte correctamente a JSON"""
        user = User.objects.create_user(
            username="juan",
            email="juan@ejemplo.com",
            password="password123"
        )
        
        serializer = User_serializer(user)
        data = serializer.data
        
        self.assertEqual(data['username'], "juan")
        self.assertEqual(data['email'], "juan@ejemplo.com")

        # Password no debe estar en la respuesta (write_only)
        self.assertNotIn('password', data)
        print("✅ ¡Serialización User→JSON correcta!")
    
    # ✅ TEST 3: Creación (JSON → User)
    def test_creacion_user_desde_json(self):
        """Verificar que podemos crear un User desde JSON"""
        serializer = User_serializer(data=self.valid_user_data)
        
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid, f"Errores: {serializer.errors}")
        
        user = serializer.save()
        
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@ejemplo.com')
        self.assertTrue(user.check_password('testpass123'))
        print("✅ ¡Creación User desde JSON correcta!")
    
    # ✅ TEST 4: Validaciones
    def test_validacion_username_obligatorio(self):
        """Verificar que username es obligatorio"""
        invalid_data = {
            'email': 'test@ejemplo.com',
            'password': 'password123'
        }
        
        serializer = User_serializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
        print("✅ ¡Validación username obligatorio funciona!")
    
    def test_validacion_email_valido(self):
        """Verificar que el email debe tener formato válido"""
        invalid_data = {
            'username': 'testuser',
            'email': 'email-invalido',
            'password': 'password123'
        }
        
        serializer = User_serializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        print("✅ ¡Validación email funciona!")
    
    def test_validacion_username_unico(self):
        """Verificar que username debe ser único"""
        # Crear primer usuario
        User.objects.create_user(
            username='usuarioexistente',
            email='existente@ejemplo.com',
            password='password123'
        )
        
        # Intentar crear segundo con mismo username
        duplicate_data = {
            'username': 'usuarioexistente',  # Mismo username
            'email': 'otro@ejemplo.com',
            'password': 'password456'
        }
        
        serializer = User_serializer(data=duplicate_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
        print("✅ ¡Validación username único funciona!")
    
    # ✅ TEST 5: Actualización
    def test_actualizacion_user_sin_password(self):
        """Verificar actualización sin cambiar password"""
        user = User.objects.create_user(
            username='original',
            email='original@ejemplo.com',
            password='password123'
        )
        
        update_data = {
            'username': 'actualizado',
            'email': 'actualizado@ejemplo.com'
        }
        
        serializer = User_serializer(user, data=update_data)
        self.assertTrue(serializer.is_valid(), f"Errores: {serializer.errors}")
        
        updated_user = serializer.save()
        
        self.assertEqual(updated_user.username, 'actualizado')
        self.assertEqual(updated_user.email, 'actualizado@ejemplo.com')
        self.assertTrue(updated_user.check_password('password123'))  # Password no cambió
        print("✅ ¡Actualización sin password funciona!")
    
    def test_actualizacion_user_con_password(self):
        """Verificar actualización cambiando password"""
        user = User.objects.create_user(
            username='testuser',
            email='test@ejemplo.com',
            password='passwordviejo'
        )
        
        update_data = {
            'username': 'testuser',
            'email': 'test@ejemplo.com',
            'password': 'passwordnuevo'
        }
        
        serializer = User_serializer(user, data=update_data)
        self.assertTrue(serializer.is_valid(), f"Errores: {serializer.errors}")
        
        updated_user = serializer.save()
        
        self.assertTrue(updated_user.check_password('passwordnuevo'))
        self.assertFalse(updated_user.check_password('passwordviejo'))
        print("✅ ¡Actualización con password funciona!")
    
    # ✅ TEST 6: Campos específicos
    def test_password_es_write_only(self):
        """Verificar que password es de solo escritura (no aparece en lectura)"""
        user = User.objects.create_user(
            username='testuser',
            email='test@ejemplo.com',
            password='password123'
        )
        
        serializer = User_serializer(user)
        data = serializer.data
        
        self.assertNotIn('password', data)
        print("✅ ¡Password es write_only!")
    
    def test_campos_correctos_en_serializador(self):
        """Verificar que el serializador tiene los campos correctos"""
        serializer = User_serializer()
        fields = serializer.get_fields()
        
        expected_fields = ['username', 'email', 'password']
        for field in expected_fields:
            self.assertIn(field, fields)
        print("✅ ¡Campos del serializador correctos!")


