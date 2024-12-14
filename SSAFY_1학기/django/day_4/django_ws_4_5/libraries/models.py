from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        API_KEY = 'ttbrlawjsdlf131545002'

        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'MaxResults': 10,
            'OutPut': 'JS',
            'SearchTarget': 'Book',
            'Version': 20131101
        }
        response = requests.get(API_URL,params=params)
        data = response.json()

        for item in data:
            my_model = cls(field1=item['field1'], field2=item['field2'])
            my_model.save()