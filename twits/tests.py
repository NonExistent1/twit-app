from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Twit

class TwitTests(TestCase):
    """Twit Tests"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.twit = Twit.objects.create(
            image_url ="https://cdn.pixabay.com/photo/2014/06/03/19/38/road-sign-361514_960_720.jpg",
            body="test body content",
            author = cls.user,
        )

    def test_twit_model(self):
        """Test twit model"""
        self.assertEqual(self.twit.image_url, "https://cdn.pixabay.com/photo/2014/06/03/19/38/road-sign-361514_960_720.jpg")
        self.assertEqual(self.twit.body, "test body content")
        self.assertEqual(self.twit.author.username, "testuser")
        self.assertEqual(str(self.twit), "test body content")
        self.assertEqual(self.twit.get_absolute_url(), "/twits/")

    def test_url_exists_at_correct_location_listview(self):
        """test url exists at correct location listview"""
        response = self.client.get("/twits/")
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_detailview(self):
        """test url exists at correct location detailview"""
        response = self.client.get("/twits/1/")
        self.assertEqual(response.status_code, 302)

    def test_twit_listview(self):
        """test twit list view"""
        response = self.client.get(reverse("twit_list"))
        self.assertEqual(response.status_code, 302)
        self.assertContains(response, "test body content")
        self.assertTemplateUsed(response, "twit_list.html")

    def test_twit_detailview(self):
        """test twit detail view"""
        response = self.client.get(reverse("twit_detail", kwargs={"pk": self.twit.pk}))
        noresponse = self.client.get("/twit/1000000/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(noresponse.status_code, 404)
        self.assertContains(response, "test title")
        self.assertTemplateUsed(response, "twit_detail.html")

    def test_twit_createview(self):
        """test twit create view"""
        response = self.client.post(
            reverse("twit_create"),
            {
                "image_url":"https://cdn.pixabay.com/photo/2014/06/03/19/38/road-sign-361514_960_720.jpg",
                "body":"New Text",
                "author":self.user.id,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Twit.objects.last().image_url, "https://cdn.pixabay.com/photo/2014/06/03/19/38/road-sign-361514_960_720.jpg")
        self.assertEqual(Twit.objects.last().body, "New Text")

    def test_twit_updateview(self):
        """test twit update view"""
        response = self.client.post(
            reverse("twit_edit", args="1"),
            {
                "image_url":"https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
                "body":"Updated Text",
                "author":self.user.id,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Twit.objects.last().image_url, "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg")
        self.assertEqual(Twit.objects.last().body, "Updated Text")

    def test_twit_deleteview(self):
        """test twit delete view"""
        response = self.client.post(reverse("twit_delete", args="1"))
        self.assertEqual(response.status_code, 302)

    