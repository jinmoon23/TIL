from django.contrib import admin
# 이거 import 하는거 깜빡했다!
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(User, UserAdmin)
