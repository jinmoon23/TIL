from django.db import models

# Create your models here.
class Keyword(models.Model):
    # 검색할 키워드명
    name = models.TextField()
    # 추가된 날짜
    created_at = models.DateField(auto_now_add=True)

class Trend(models.Model):
    # 검색을 수행한 키워드명
    name = models.TextField()
    # 검색 결과 수
    result = models.IntegerField()
    # 검색 기간
    search_period = models.TextField()
    # 추가된 날짜
    created_at = models.DateField(auto_now_add=True)