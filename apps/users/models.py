from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    website = models.URLField(max_length=200, blank=True)
    photo = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        """Return username."""
        return self.user.username


