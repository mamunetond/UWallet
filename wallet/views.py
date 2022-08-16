from django.http import HttpResponse
from django.shortcuts import render
from .templates.income.Income import RegisterIncome

def index(request):
    return HttpResponse('HOME PAGE')

def income_view(request):
    register_income = RegisterIncome()
    return render(request, 'income/register_income.html', {'register_income': register_income})