from django.db import models

# Create your models here.
class Weather(models.Model):
    dt_txt = models.DateTimeField()
    temp = models.FloatField()
    feels_like = models.FloatField()