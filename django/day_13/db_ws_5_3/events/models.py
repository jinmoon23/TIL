from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.TextField(max_length=100)
    date = models.DateField()
    location = models.TextField()

class Participant(models.Model):
    events = models.ManyToManyField(Event,related_name='participants')
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phone_number = models.TextField(max_length=15)
    registeration_date = models.DateTimeField(auto_now_add=True)
