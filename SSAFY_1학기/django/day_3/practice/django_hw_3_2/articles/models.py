from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField()