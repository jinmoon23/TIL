from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.TextField(max_length=100)
    age = models.IntegerField()
    
class Product(models.Model):
    name = models.TextField(max_length=100)
    # max_digits는 전체 자릿수를 의미하고, decimal_places는 소수점 이하 자릿수를 의미함.
    # 따라서 max_digits=2 라고 하면 소수점 앞뒤를 합쳐서 두 자릿수만 허용되는 상황인데, 
    # 13.34는 총 4자리이므로 이를 저장할 수 없어 오류가 발생함.
    price = models.DecimalField(max_digits=4,decimal_places=2)
    buy_list = models.ManyToManyField(Customer)