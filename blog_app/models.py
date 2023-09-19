from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
     logo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
