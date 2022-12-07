from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import PostList, PostDetail, PostLike


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_like_url_is_resolved(self):
        url = reverse('post_like')
        self.assertEquals(resolve(url).func.view_class, PostLike)

    def test_postview_url_is_resolved(self):
        url = reverse('post_detail', args=['post-id'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)
