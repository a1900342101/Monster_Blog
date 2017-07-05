# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.contrib import admin

# Register your models here.

from django.contrib import admin
from models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = ('title',)

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'js/editor/kindeditor-min.js',
            'js/editor/lang/zh_CN.js',
            'js/editor/config.js',
        )

