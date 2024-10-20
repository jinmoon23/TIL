from django.db import models

# Create your models here
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    product = models.ManyToManyField(Product,through='Order',related_name='customers')

    def __str__(self):
        return self.name

# quantity나 order_date 같은 추가적 fields를 생성하지 않아도 된다면
# order 중개모델을 설정하지 않고 manytomanyfield로도 M:N관계 설정이 충분함.
# 하지만 추가적인 fields 설정이 필요한 경우이기 때문에 through='Order' 인자를 추가하고
# order 중개모델을 설정하는 것임.
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField()