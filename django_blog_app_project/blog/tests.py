from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username='testuser', email = 'test@email.com',password='secret'
        )
        cls.post = Post.objects.create(
            title = "A good title",
            body = 'Nice content',
            author = cls.user,
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, 'Nice content')
        self.assertEqual(self.post.author.username,'testuser')
        self.assertEqual(str(self.post),'A good title')
        self.assertEqual(self.post.get_absolute_url(),'/post/1/')
        
    def test_home_page_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_post_page_location(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code,200)
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Nice content')
        self.assertTemplateUsed(response,'home.html')
        
    