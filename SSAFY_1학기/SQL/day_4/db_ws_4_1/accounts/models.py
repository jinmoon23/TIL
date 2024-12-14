from django.db import models
# 1. AbstractUser 상속받는 User 클래스 생성
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
