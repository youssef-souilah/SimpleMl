from django.db import models
# Create your models here.

class Image (models.Model):
    name = models.TextField(unique=True)
    image = models.ImageField(upload_to="images")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name = self.name 
        self.file_path = self.image.url 
        super().save(*args, **kwargs)
