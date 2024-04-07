"""
Jordyn Kuhn
CIS 218
4-7-2024
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpPageTests(TestCase):
    """Sign up Page Tests"""

    def test_url_exists_at_correct_location_signupview(self):
        """Test url exists at correct location signup view"""
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        """Test signup View Name"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username":"testuser",
                "email":"testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
                "first_name": "test",
                "last_name": "test",
            }
        )

        self.assertEqual(response.status_code, 302)        
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")

class UpdatePageTests(TestCase):
    """Update Account Page Tests"""
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="testuser", email="test@email.com", password="secret"
    )

    def test_url_exists_at_correct_location_updateview(self):
        """Test url exists at correct location update view"""
        response = self.client.get("/accounts/1/update", args="1")
        self.assertEqual(response.status_code, 302)

    def test_update_form(self):
        response = self.client.post(
            reverse("account_update", args="1"),
            {
                "username":"testuser2",
                "email":"testuse2r@email.com",
                "first_name": "test2",
                "last_name": "test2",
            }
        )

        self.assertEqual(response.status_code, 302)        
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser2")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuse2r@email.com")
        self.assertEqual(get_user_model().objects.all()[0].first_name, "test2")
        self.assertEqual(get_user_model().objects.all()[0].last_name, "test2")