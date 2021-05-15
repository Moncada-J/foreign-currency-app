from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<nav><img src="https://imgur.com/PPaJpDC.png"><h3>Collect Foreign Currencies</h3></nav>')

def about(request):
    return HttpResponse('<h2>About the Currencies</h2>')