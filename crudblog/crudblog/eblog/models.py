from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class User(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    user = models.TextField('username')
    date_added = models.DateTimeField('date_added', auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.user
