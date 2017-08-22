from django.contrib import admin
default_encoding = 'utf-8'

# Register your models here.
from django.conf import settings
from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'title')
    list_display_links = ('id', 'content', 'title')


    class Media:
        js = (
            '/static/kindeditor-4.1.10/kindeditor-min.js',
            '/static/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/kindeditor-4.1.10/config.js',
        )


admin.site.register(article, ContactAdmin)
admin.site.register(Category)
