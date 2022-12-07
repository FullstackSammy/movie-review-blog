from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Post, Comment


class PostModelTestCase(TestCase):
    def setUp(self):
        # Disconnect signal from haystack, no need to generate
        # index for test generated articles
        # apps.get_app_config('haystack').signal_processor.teardown()
        self.user = User.objects.create_user(
            username="admin", email="admin@admin.com", password="bauer144"
        )
        self.post = Post.objects.create(
            title="Test title",
            content="Test content",
        )

    def test_post_create_01(self):
        testpost = get_object_or_404(Post, title="Test title")
        self.assertEqual(self.post.content, "Test content")

        self.assertNotEqual(self.post.content, "contentz")

        self.assertEqual(self.post.title, "Test title")

        self.assertEqual(self.post.created_on, testpost.created_on)

    def test_add_comment(self):
        post = get_object_or_404(Post, title="Test title")
        self.comment = Comment.objects.create(
            post=post, body="This is my comment"
        )
        self.assertEqual(self.comment.body, "This is my comment")

        self.assertNotEqual(self.comment.body, "Not my comment")

        self.assertIsNotNone(self.comment.post_id)

        self.assertEqual(self.comment.post_id, post.id)

        self.assertIsNotNone(self.comment.created_on)

    def test_add_like(self):
        post = get_object_or_404(Post, title="Test title")
        post.likes.add(self.user)

        self.assertEqual(post.content_one.number_of_likes(), 1)
