"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # include函数允许引用其他URLconfs。Django遇到这个函数的时候，
    # 会截断和其匹配的url部分，将剩余的字符串发送到URLconf再处理。
    # 当包括其它 URL 模式时你应该总是使用 include()
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
