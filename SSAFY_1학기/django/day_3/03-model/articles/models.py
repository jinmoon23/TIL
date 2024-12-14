from django.db import models

# Create your models here.

class Article(models.Model):
    # 인스턴스 생성과정
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)