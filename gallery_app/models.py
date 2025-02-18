from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='photos_for_gallery_media/', blank=True, null=True)