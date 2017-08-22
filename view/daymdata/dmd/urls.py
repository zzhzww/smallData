from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contents', views.content, name='content'),
    url(r'^$',views.index,name='index'),
        ]
