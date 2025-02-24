from django.db import models
from django.utils import timezone  # Keeping this in case you need it later

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()  # Ensures valid email input
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Removed default

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Cart(models.Model):
    user = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Removed default

    def __str__(self):
        return f"{self.user} - {self.product}"


class Services(models.Model):
    name = models.CharField(max_length=100)
    queries = models.TextField()
    suggestions = models.TextField()
    description = models.TextField(default="")  # Default empty string to avoid migration issues
    created_at = models.DateTimeField(auto_now_add=True)  # Removed default

    def __str__(self):
        return self.name


class About(models.Model):
    firm = models.CharField(max_length=100)  # Renamed for consistency
    location = models.TextField()
    suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Removed default

    def __str__(self):
        return self.firm  # Changed from 'self.name' to 'self.firm'
