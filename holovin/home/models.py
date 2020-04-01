from django.db import models

class HomeImage(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    image_file = models.FileField(upload_to='homeimages/', blank=True, null=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
