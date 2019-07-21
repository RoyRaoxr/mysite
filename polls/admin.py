from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question

# 告诉管理界面Question需要被管理
admin.site.register(Question)

