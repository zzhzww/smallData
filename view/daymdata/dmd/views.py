# -*- coding:utf-8 -*-
from django.shortcuts import render
import logging
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from .models import article

logger = logging.getLogger('dmd.views')
def gloabe_setting(request):
    return {"SITE_NAME": settings.SITE_NAME}


def index(request):
    articlelist =article.objects.all()
    template = loader.get_template('pc/index.html')
    context = {}
    context['name'] = u"首页"
    context['articlelist'] = articlelist
    print context

    return HttpResponse(template.render(context, request))

def content(request):
    try:
        request.encoding='utf-8'
        get=request.GET.get('id',None)
        articleInfo = article.objects.get(id=get)
        context = {}
        context['article'] = articleInfo
        template = loader.get_template('pc/content.html')

        return HttpResponse(template.render(context, request))
    except article.DoesNotExist:
        return render(request,'pc/content.html',{'reason': '没有找到文章'})




def base(request):
    template = loader.get_template('pc/base.html')
    context = {}


    return HttpResponse(template.render(context, request))