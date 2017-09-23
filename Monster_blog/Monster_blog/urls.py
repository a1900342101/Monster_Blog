# -*-coding:utf-8 -*-
"""Monster_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from blog import views
from blog.uploads import upload_image
from django.conf.urls import url
from django.conf import settings # addition
from django.views import static  # 引入view对象
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^blog/(?P<id>[0-9]{1}).html$',views.view),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),  # 上传url
    url(r"^uploads/(?P<path>.*)$", static.serve, {"document_root": settings.MEDIA_ROOT},),  # 访问上传后文件url
]
