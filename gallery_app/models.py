from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Image(models.Model):
    image = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='photos_for_gallery_media/', blank=True, null=True)