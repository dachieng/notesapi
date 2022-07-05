from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from noteapi.models import Note
from users.models import User


class TestNote(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="oloodorcas99@gmail.com", username="dorcas",
            password="teddy123")
        self.note = Note.objects.create(author_id=1, title="title", content="this is the conent",
            )

    
    # test for jwt authorization
    @property
    def bearer_token(self):
        user_auth = User.objects.get(id=1)
        refresh_token = RefreshToken.for_user(user_auth)
        return {"HTTP_AUTHORIZATION":f'Bearer {refresh_token.access_token}'}

    def test_note_content(self):
        self.assertIsInstance(self.note, Note)
        self.assertEqual(self.note.slug, 'title')
        self.assertEqual(self.note.author.username, 'dorcas')

    
    def test_note_str_return(self):
        note = self.note
        self.assertEqual(str(note), 'title')

    
    def test_get_note_api_request(self):
        self.client.login(email=self.user.email, password='teddy123')

        url = reverse("notes:notes")

        response = self.client.get(url, format="json", **self.bearer_token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_note_api_request(self):
        self.client.login(email=self.user.email, password='teddy123')

        url = reverse("notes:notes")

        data = {
            "author":1,
            "title":"title",
            "content":"this is the content"
        }

        response = self.client.post(url, data, format="json", **self.bearer_token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
