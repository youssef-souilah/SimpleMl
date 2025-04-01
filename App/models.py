from django.db import models
# Create your models here.


class Image (models.Model):
    name = models.TextField(unique=True)
    image = models.ImageField(upload_to="images")
    type=models.BooleanField(null=False) #0 for cat & 1 for dog
    def __str__(self):
        return self.name 
    
