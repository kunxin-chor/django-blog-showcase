from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your tests here.
class PostTestCase(TestCase):
    
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        
    
    def test_can_get_excerpt(self):
        p = Post()
        p.title = "Hello World"
        p.content = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        excerpt = p.get_excerpt()
        self.assertEqual("Hello World - ABCDEFGHIJKLMNOPQRSTUVWXY", excerpt)
    
    def test_can_get_excerpt_if_content_shorter_than_25_characters(self):
        p = Post()
        p.title = "Hello World"
        p.content = "ABCD"
        excerpt = p.get_excerpt()
        self.assertEqual("Hello World - ABCD", excerpt)
        
    def test_can_get_excerpt_if_no_title(self):
        p = Post()
        p.title = None
        p.content = "ABCD"
        excerpt = p.get_excerpt()
        self.assertEqual("N/A", excerpt)
        
    def test_can_save_post(self):
        p = Post()
        p.title = "Hello World"
        p.content = "ABCDE"
        # setup the foreign key relationship
        p.author = self.user
        p.save()
        
        fetched_post = Post.objects.get(pk=p.id)
        self.assertNotEqual(None, fetched_post)
        self.assertEqual("Hello World", fetched_post.title)
        self.assertEqual("ABCDE", fetched_post.content)
        
    def test_can_find_posts(self):
        # create test posts
        for i in ['A', 'B', 'C']:
            p = Post()
            p.title = i
            p.content = i
            p.author = self.user
            p.save()
        
        results = Post.search("B") 
        self.assertEquals(1, results.count())
        self.assertEqual(results.first().title, "B")
        self.assertEqual(results.first().content, "B")
        
    def test_cannot_find_posts(self):
         # create test posts
        for i in ['A', 'B', 'C']:
            p = Post()
            p.title = i
            p.content = i
            p.author = self.user
            p.save()
  
        results = Post.search("D")
        self.assertEquals(0, results.count())
        
        results = Post.search(None)
        self.assertEquals(0, results.count())
 

        
        