from django.shortcuts import render
import datetime
import string


# Create your views here.

def doter(request):
    return render(request, 'page.html' and 'text.html')


def text(request):
    return render(request, 'text.html', {"date": datetime.datetime.now()})


def page(request):
    return render(request, 'page.html', {"ascii": string.ascii_letters})
