from django.test import TestCase
from . models import Post


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')

    def test_one_equal_two(self):
        self.assertTrue(1 ==2)
