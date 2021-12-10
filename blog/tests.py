from django.test import TestCase
from . models import Post


def test_my():
    assert 1 == 1


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')
