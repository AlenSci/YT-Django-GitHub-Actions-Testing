from django.test import TestCase
from . models import Post


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')

    def test_my(self):
        assert 1 == 1

    def test_my2(self):
        assert 1 == 2