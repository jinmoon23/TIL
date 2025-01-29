from django.db import models
# 1. AbstractUser import
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 2. class 정의
class User(AbstractUser):
    pass