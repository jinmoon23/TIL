from django.contrib import admin
# 3. 관리자 페이지에서 관리할 수 있도록 등록하기 위한 import
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
# 4. 관리자 페이지에서 관리할 수 있도록 등록
admin.site.register(User,UserAdmin)