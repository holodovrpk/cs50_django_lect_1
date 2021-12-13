from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def alex(request):
    return HttpResponse("Hello, Alex!")

def bob(request):
    return HttpResponse("Hello, Bob!")

"""def privet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")"""
def privet(request, name):
    return render(request, "hello/privet.html", {
        "name":name.capitalize()
    })