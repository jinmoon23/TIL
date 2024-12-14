from django.db import models
from accounts.models import User
from django.conf import settings
# Create your models here.
class Article(models.Model):
    # user에 대한 정보 외래키로 설정
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # 역참조(1이 N을 참조)할 경우
    # article.comment_set.all() 또는 .get(pk=x)
    # 여기서 comment_set이 역참조 매니저에 접근하는 방법
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # user에 대한 정보를 외래키로 설정
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # ForeignKey(상대 모델 클래스, 상대 모델 클래스가 삭제되었을 때 어떻게 처리할 것인가?)
    # _id를 모델 설정시 추가하지 않더라도 데이터베이스에 자동으로 추가됨 ^_^
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)