from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from works.models import About
from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        'title': 'Welcome to home page'
    }
    # messages.success(request, 'Profile details updated.')
    return render(request, 'index.html', context)
    # return HttpResponse('this is home page')


def about(request):
    if request.method == "POST":
        aboutinfo = request.POST.get('about')
        about = About(about=aboutinfo)
        about.save()
        messages.success(request, 'About Updated Successfully.')

    abouts = About.objects.all()
    
    context = {
        'title': 'About Us',
        'abouts': abouts
    }
    return render(request, 'about.html', context)
    # return HttpResponse('this is about page')
