# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib import admin

# create the blog model
sex_choices = (
        ('f','famale'),
        ('m','male'),
    )
class Author(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10,choices=sex_choices)
    instrument = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    index_text =models.TextField() 
    body = models.TextField()
    times = models.DateTimeField()
    comment = models.IntegerField()
    likes = models.IntegerField()
    def __unicode__(self):
        return self.title

# set the admin page for BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','times')

# register the model (especially important
admin.site.register(Author)
admin.site.register(BlogPost)
