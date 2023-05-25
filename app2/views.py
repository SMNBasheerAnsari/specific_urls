from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def str3(request):
    return HttpResponse("this is string of app2")
def str4(request):
    return HttpResponse("this is another string of app2")