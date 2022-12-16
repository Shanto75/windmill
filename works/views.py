from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from works.models import About
# Create your views here.


def index(request):
    context = {
        'title': 'Welcome to home page'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is home page')


def about(request):
    if request.method == "POST":
        aboutinfo = request.POST.get('about')
        about = About(about=aboutinfo)
        about.save()

    context = {
        'title': 'About Us'
    }
    return render(request, 'about.html', context)
    # return HttpResponse('this is about page')
