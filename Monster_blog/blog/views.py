# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response 
from blog import models


def index(req):
    blogs = models.BlogPost.objects.all()
    return render_to_response('index.html', {'blogs': blogs})

def view(req,id):
    blog = models.BlogPost.objects.get(id=id)
    return render_to_response('view.html',{'blog':blog})

def _404(req):
    return render_to_response('404.html',{'title':'Not found'})