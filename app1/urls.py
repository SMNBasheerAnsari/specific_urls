app_name='app1_urls'
from django.urls import path
from app1.views import *
urlpatterns=[
    path('str1/',str1,name='str1'),
    path('str2/',str2,name='str2'),
]