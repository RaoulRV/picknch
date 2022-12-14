from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    item = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    short_description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.item

    def number_of_likes(self):
            return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item)
        return super().save(*args, **kwargs)
