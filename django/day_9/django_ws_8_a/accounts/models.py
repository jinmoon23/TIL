from django.db import models
# 1. AbstractUser import
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 2. 추상 유저 클래스 작성 -> 추가적으로 필드를 작성하지 않는다.
# 그 이유는 AbstractUser 클래스는 AbstractBaseUser를 상속받기 때문에 이미 필요한 필드가 정의되어 있기 때문.
class User(AbstractUser):
    pass
