from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

def about(request):
    return HttpResponse('this is about page')