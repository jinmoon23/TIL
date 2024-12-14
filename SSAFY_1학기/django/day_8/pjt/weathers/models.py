from django.db import models

# Create your models here.
class Weather(models.Model):
    date = models.DateField()
    temp_high_f = models.IntegerField()
    temp_avg_f = models.IntegerField()
    temp_low_f = models.IntegerField()
    dew_point_high_f = models.IntegerField()
    dew_point_avg_f = models.IntegerField()
    dew_point_low_f = models.IntegerField()
    humidity_high_percent = models.FloatField()
    humidity_avg_percent = models.FloatField()
    humidity_low_percent = models.FloatField()
    sea_level_p_high_inches = models.FloatField()
    sea_level_p_avg_inches = models.FloatField()
    sea_level_p_low_inches = models.FloatField()
    events = models.CharField(max_length=300)