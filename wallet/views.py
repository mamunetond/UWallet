from django.http import HttpResponse
from django.shortcuts import render, redirect
from .templates.income.Income import RegisterIncome
from .models import Income

def home(request):
    return render(request, 'home/home.html')

def income_view(request):
    incomes = Income.objects.all()
    return render(request, 'income/register_income.html', {'incomeslist': incomes})
    #register_income = RegisterIncome()
    #return render(request, 'income/register_income.html', {'register_income': register_income})
    
def registerincomes(request):
    value_income= request.POST['intvalue_income']
    type_income= request.POST['txttype_income']
    detail_income= request.POST['txtdetail_income']
    date_income=request.POST['datedate_income']
    
    income = Income.objects.create(value_income= value_income, type_income= type_income, detail_income= detail_income, date_income= date_income)
    return redirect('income/')

def academy(request):
    return render(request, 'academy/academy.html')

def feed(request):
    return render(request, 'feed/feed.html')