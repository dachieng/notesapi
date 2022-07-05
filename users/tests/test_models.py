from rest_framework.test import APITestCase

from users.models import User


class TestUserModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="dorcas", email="oloodorcas99@gmail.com",
                password="teddy@123")
        self.superuser = User.objects.create_superuser(username="mitchell", email="oloomitchell@gmail.com",
                password="teddy@123")

        
    def test_create_user(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, "dorcas")
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)

    def test_create_superuser(self):
        self.assertIsInstance(self.superuser, User)
        #self.assertTrue(self.superuser.is_staff)
        #self.assertTrue(self.superuser.is_superuser)


    def test_username_not_provided(self):
        self.assertRaises(ValueError, User.objects.create_user, 
                username="", email="oloodorcas99@gmail.com", password="teddy@123")
    
    def test_email_not_provided(self):
        self.assertRaises(ValueError, User.objects.create_user, 
                username="dorcas", email="", password="teddy@123")

    
    def test_error_if_is_staff_set_to_false(self):
        self.assertRaises(ValueError, User.objects.create_superuser, 
            username="dorcas", email="oloodorcas99@gmail.com", password="teddy123", is_staff=False)

    
    def test_error_if_is_superuser_set_to_false(self):
        self.assertRaises(ValueError, User.objects.create_superuser, 
            username="dorcas", email="oloodorcas99@gmail.com", password="teddy123", is_superuser=False)
