# -*- coding: utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^list/$', views.list, name='list'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^uploadform/$', views.uploadform, name='uploadform'),    
    url(r'uploadsuccess/$', views.uploadsuccess, name='uploadsuccess')    

]
