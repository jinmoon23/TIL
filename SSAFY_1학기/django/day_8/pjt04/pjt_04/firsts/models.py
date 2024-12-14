from django.db import models

# Create your models here.
class Weather(models.Model):
    date = models.DateField()
    temp_avg_f = models.IntegerField()
    events = models.CharField(max_length=300, blank=True,null=True)