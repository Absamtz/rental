# Create your models here.
# models.py

from django.db import models
# from django.contrib.auth.models import User  # Import the User model
from django.conf import settings

class Image(models.Model):
    name = models.CharField(max_length=100 )
    image_name = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=100, default='Name')
    location = models.CharField(max_length=100, default='location')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField( default="Descriptions")
    image_name = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user}"