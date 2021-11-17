from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='shahdalkhatib95@gmail.com',
            email='shahdalkhatib95@gmail.com',
            password='1234'
        )

        self.post = Snack.objects.create(
            name='pancake',
            description='food',
            purchaser=self.user
        )

    
    def test_string_representation(self):
        post = Snack(name='name')
        self.assertEqual(str(post), post.name)


#####################
    def test_all_fields(self):
        
        self.assertEqual(str(self.post), 'pancake')
        self.assertEqual(f'{self.post.purchaser}', 'shahdalkhatib95@gmail.com')
        self.assertEqual(self.post.description, 'food')

   ###########################

    def test_blog_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details_view(self):
        response = self.client.get(reverse('snack_detail', args='1'))
        self.assertEqual(response.status_code, 200)



        ####### 

        
    def test_blog_update_view(self):
        response = self.client.post(reverse('snack_update', args='1'), {
            'name': 'chips',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')

    ############

    def test_home_status(self):
        expected = 200
        url = reverse('snack_list')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        actual = 'snacks/snack_list.html'
        self.assertTemplateUsed(response, actual)
    
   ################

    def test_create_view(self):
        response = self.client.post(reverse('snack_create'), {
            'name': 'chips',
            'purchaser': self.user,
            'description' :'healthy food',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')
        self.assertContains(response, 'healthy food')
        self.assertContains(response, 'shahdalkhatib95@gmail.com')

    def test_delete_view(self):
        response = self.client.get(reverse('snack_delete', args='1'))
        self.assertEqual(response.status_code, 200)