from .models import Post
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        excepted_object_name = f'{post.text}'
        self.assertEqual(excepted_object_name,"just a test")

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code,200)

    def test_view_url_name(self):
        resp = self.client.get(reverse('post_list'))
        self.assertEqual(resp.status_code,200)

    def test_view_template(self):
        resp = self.client.get(reverse('post_list'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'posts/list.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absoult_url(),"/blog/1/")


    def test_create_post(self):
        response = self.client.post(reverse("blog_new")),{
            'title':'new post',
            'body' :'body new post',
            'author':self.user.id,
        
        }
        self.assert_Equal(response.status_code,302 )
        self.assertEqual(Post.objects.last().title,"new post")
        self.assertEqual(Post.objects.last.title,"body new post")