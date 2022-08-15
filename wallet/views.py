from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to home page <h1>')
    return render(request,'home.html', {'name': 'Greg Lim'})

def income(request):
    return render(request, 'income.html', {'name': 'Greg Lim'})

def cost(request):
    return render(request, 'cost.html', {'name': 'Greg Lim'})