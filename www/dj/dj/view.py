#-*- coding:utf-8 -*-
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = "hello word"
    return render (request, "hello.html",context)
