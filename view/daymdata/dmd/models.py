# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=100, verbose_name='分类排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

        def __unicode__(self):
            return str(self.name)



class article(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    content = models.TextField(verbose_name='文章内容')
    time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

        def __unicode__(self):
            return str(self.title)


