app_name='app2_urls'
from django.urls import path
from app2.views import *
urlpatterns=[
    path('str3/',str3,name='str3'),
    path('str4/',str4,name='str4'),
]


