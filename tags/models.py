from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    