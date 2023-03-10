from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def baby(request):
    return HttpResponse('<h1>how are you baby</h1>)

def Bhavana(request):
    return HttpResponse('<marquee><h1> Bhavana </h1>')
