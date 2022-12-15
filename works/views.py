from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Welcome to home page'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is home page')

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'about.html', context)
    # return HttpResponse('this is about page')