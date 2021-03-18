from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'index.html')

def currentDate(request):
    context = {
        "time": strftime('%I: %M %p', gmtime()),
        "date": strftime('%Y-%B-%A-%d', gmtime())
    }
    return render(request, 'index.html', context)
