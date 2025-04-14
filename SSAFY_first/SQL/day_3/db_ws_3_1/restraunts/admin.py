from django.contrib import admin
from .models import Restraunt,Menu,Category
# Register your models here.
admin.site.register([Restraunt,Menu,Category])