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
        
    
    def test_delete_more_deep(self):
        """
        To test the delete process, we check if the deleted things was deleted or not by enssure it not contain 
        in the desired page.
        """
        post_response = self.client.post(reverse('delete', args='1'), follow=True)
        self.assertRedirects(post_response, reverse('list'), status_code=302)
        del_res=self.client.get(reverse('list'))
        self.assertNotContains(del_res,'Kuftah')


class Test_names_of_routes(TestCase):
    """
    This test is valid just for home page and create page,
    Becuase they are static routes. Where Update and details and delete are dynamic routes and they are using the model and PK
    """
   
    def test_home_list(self):
        """
        Check for the right path to the desired page
        """
        url = reverse('list')
        response = self.client.get(url)
        actual= 'list.html'
        self.assertTemplateUsed(response,actual)
    
    def test_Create_route(self):
        """
        Check for the right path to the desired page
        """
        url = reverse('create')
        response = self.client.get(url)
        actual= 'create.html'
        self.assertTemplateUsed(response,actual)
    
   
    