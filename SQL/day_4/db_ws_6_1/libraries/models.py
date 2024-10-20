from django.db import models
from django.conf import settings
# Create your models here.
class Book(models.Model):
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField()
    genre = models.TextField()

class Author(models.Model):
    subscribed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribe_users')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nickname = models.TextField(max_length=20)