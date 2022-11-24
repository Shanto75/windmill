from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'x':5
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is home page')

def about(request):
    return HttpResponse('this is about page')