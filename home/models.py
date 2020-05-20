from django.db import models
from django.conf import settings
from django.utils import timezone

class HomeImage(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    image_file = models.FileField(upload_to='homeimages/', blank=True, null=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300, blank=True, null=True)
    text = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)
    image_file = models.FileField(upload_to='postimages/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

