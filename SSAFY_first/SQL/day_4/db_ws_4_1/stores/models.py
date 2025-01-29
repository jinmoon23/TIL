from django.db import models
# 3. conf & settings import 
from django.conf import settings
# Create your models here.
class Store(models.Model):
    # 4. user의 경우 특수하다!
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address = models.TextField(max_length=100)
    is_franchise = models.BooleanField()
    def __str__(self):
        return f'{self.address}점'
    
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    adult = models.BooleanField()