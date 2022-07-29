import pytest
from django.contrib.auth.models import User
from django.urls import reverse

# class URLTests(TestCase):
#     def test_testhomepage(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1

@pytest.mark.django_db
def test_view(client):
   url = reverse('homepage-url')
   response = client.get(url)
   assert response.status_code == 200