from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
app_name = 'blog'


class Post(models.Model):
    """
    Post Model
    """
    HORROR = 'Horror'
    COMEDY = 'Comedy'
    SCIFI = 'Sci-fi'
    FANTASY = 'Fantasy'
    ACTION = 'Action'
    ROMANTIC = 'Romantic'
    THRILLER = 'Thriller'
    ANIME = 'Anime'
    OTHER = 'Other'

    MOVIE_GENRES = [
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (SCIFI, 'Sci-fi'),
        (FANTASY, 'Fantasy'),
        (ACTION, 'Action'),
        (ROMANTIC, 'Romantic'),
        (THRILLER, 'Thriller'),
        (ANIME, 'Anime'),
        (OTHER, 'Other')
    ]

    title = models.CharField(
        max_length=200, unique=True, default='')
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.CharField(
        max_length=50, choices=MOVIE_GENRES, default=HORROR)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        return self.genre

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Comment Model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'