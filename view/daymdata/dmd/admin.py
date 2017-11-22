# -*- coding:utf-8 -*-
from django.contrib import admin
default_encoding = 'utf-8'
from django import forms
# Register your models here.
from django.conf import settings
from django.contrib import admin
from .models import *


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class MyInvoiceAdminForm(forms.ModelForm):

    category = CustomModelChoiceField(queryset=category.objects.all())
    # category = forms.ModelChoiceField(queryset=category.objects.all())
    # def __init__(self,*args,**kwargs):
    #     super(MyInvoiceAdminForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['category'].queryset=category.objects.all()
    #     self.fields['category'].label_from_instance = lambda obj:obj.name
    class Meta:
        model = article
        fields = "__all__"

class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'catid','title',)
    list_display_links = ('id', 'title')

    form = MyInvoiceAdminForm



class Media:
        js = (
            '/static/kindeditor-4.1.10/kindeditor-min.js',
            '/static/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/kindeditor-4.1.10/config.js',
        )
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','index')
    fields = ('name','index')
    list_editable=('index',)




admin.site.register(article, ContentAdmin)
admin.site.register(category,CategoryAdmin)


