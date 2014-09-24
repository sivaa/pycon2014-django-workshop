from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def hello1(request):
    return HttpResponse("Hello World!")

def hello2(request):
    return HttpResponse("<h1>Hello World!</h1>")

def hello3(request):
    return HttpResponse("<h1>Hello World! at {} </h1>".format(datetime.now()))

def hello4(request):
    name = request.GET.get("name", "Django")
    return HttpResponse("Hello <strong>{}</strong>!".format(name))

def hello5(request):
    return render(request, "hello5.html")

def hello6(request):
    return render(request, 
                  "hello6.html",
                  {'current_time' : datetime.now() })

def hello7(request):
    name = request.GET.get("name", "Django")
    return render(request, 
                  "hello7.html",
                  {'name' : name })
