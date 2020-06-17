from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.contrib.auth.models import User
from apps.categories.models import Category

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    image_header = models.ImageField(upload_to='posts/photos')
    video_header = models.FileField(upload_to='posts/videos') 
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('title',)


    def __str__(self):
       
        return '{} by @{}'.format(self.title, self.user.username)


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

