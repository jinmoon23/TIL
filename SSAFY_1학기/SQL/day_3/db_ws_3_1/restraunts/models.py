from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=20)
    
class Restraunt(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    description = models.TextField()
    address = models.TextField(max_length=200)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

class Menu(models.Model):
    restraunt = models.ForeignKey(Restraunt,on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    price = models.IntegerField()
    is_vegan = models.BooleanField()