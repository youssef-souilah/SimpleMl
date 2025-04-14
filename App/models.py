from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Image (models.Model):
    name = models.TextField(unique=True)
    image = models.ImageField(upload_to="images")
    type=models.TextField(null=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    
User = get_user_model()

class Train(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trains')
    images = models.ManyToManyField('Image', related_name='trains')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"