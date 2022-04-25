from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="test@email.com",
            first_name="Test",
            password="foo",
            username="test_user"
        )
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', first_name='test', username='test_user', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='admin2@email.com',
            first_name='Admin',
            password='foo',
            username='admin'
        )
        self.assertEqual(admin_user.email, 'admin2@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='admin2@email.com', first_name='admin2', username='admin2', password='foo', is_superuser=False
            )
