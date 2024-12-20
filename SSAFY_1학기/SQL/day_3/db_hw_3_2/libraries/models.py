from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()
    nationality = models.TextField()
    def __str__(self):
        return f"{self.name}"
    
class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField()
    adult = models.BooleanField()
    price = models.IntegerField()