# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.http import HttpResponse        #methd 1
#from django.template import loader,Context   #methd 1

from django.shortcuts import render_to_response #mathd 2

from blog import models

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
'''
# method1
def index(req):
    t = loader.get_template('index.html')
    c = dict({}) #chuan ru shu ju 
#xuan ran ran hou return changed html 
    return HttpResponse(t.render(c))
   return HttpResponse('<title>python view.index</title> <h1>hello python</h1>')

#method 2
def index(req):
    #user = {'name':'Monster Hu','age':22,'sex':'male'}  #use complex data
    user = Person('Monster Hu',22,'male')              #use a class
    book_list = ['python','java','math']        #use a list
    return render_to_response('index.html',{'title':'home page','user':user,'book_list':book_list})

def index1(req):
    user1 = Person('',22,'male')              #use a class
    book_list = ['python1','java1','math1']        #use a list
    details = ['20','10','2017-5-29']
    return render_to_response('index.html',{'title':'my page1','likes':details[0],'comments':details[1],'time':details[2]})
'''
def index(req):
    #blogs = BlogPost.objects.filter(title='test title')
    blogs = models.BlogPost.objects.all()
    return render_to_response('index.html', {'blogs': blogs})

def view(req,id):
    blog = models.BlogPost.objects.get(id=id)
    return render_to_response('view.html',{'blog':blog})

def _404(req):
    return render_to_response('404.html',{'title':'Not found'})