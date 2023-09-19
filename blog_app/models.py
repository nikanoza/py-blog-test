from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='category_logos/', null=True, blank=True)

    def __str__(self):
        return self.title