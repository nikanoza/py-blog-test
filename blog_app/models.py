from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name