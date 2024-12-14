from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.TextField()
    isbn = models.TextField()
    pubdate = models.DateField()
    pricesales = models.IntegerField()
    sales_point = models.IntegerField()
    adult = models.BooleanField()
    description = models.TextField()