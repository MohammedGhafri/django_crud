from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post


# Create your tests here.

class for_test(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Mohammed',
            email='mghafri@gmail.com',
            password='159753'
        )

        self.snack = Post.objects.create(
            title='Kuftah',
            body= 'meat fully with some tommato and onione',
            author=self.user
        )

    def test_list(self):
        expected=200
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        url= reverse('details', args='1')
    
        response = self.client.get(url)
        expected =200
        self.assertEqual(response.status_code, expected)

    def test_updarte(self):
        url = reverse('update', args='1')
        response = self.client.post(url, {
            'title': 'Potato','body':'New body',
        })
        expected = 200
        self.assertEqual(response.status_code, expected)
        self.assertContains(response, 'Potato')
        self.assertContains(response, 'New body')

    def test_deletes_contain(self):
        url = reverse('delete', args='1')
        response = self.client.get(url, follow=True)
        self.assertContains(response, 'If you wanna delete this press <strong>OK</strong>,Else press Cancel ?')
    
    def test_delete(self):
        """
        To test the delete process, we check the redirect route
        """
        post_response = self.client.post(reverse('delete', args='1'), follow=True)
        self.assertRedirects(post_response, reverse('list'), status_code=302)

