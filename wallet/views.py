from django.http import HttpResponse
from django.shortcuts import render, redirect
from .templates.income.Income import RegisterIncome
from .models import Income
from .models import Spent
def index(request):
    return HttpResponse('HOME PAGE')

def income_view(request):
    incomes = Income.objects.all()
    return render(request, 'income/register_income.html', {'incomeslist': incomes})
    
def registerincomes(request):
    value_income= request.POST['intvalue_income']
    type_income= request.POST['txttype_income']
    detail_income= request.POST['txtdetail_income']
    date_income=request.POST['datedate_income']
    
    income = Income.objects.create(value_income= value_income, type_income= type_income, detail_income= detail_income, date_income= date_income)
    return redirect('/income/')

def deleteincome(request, codigo):
    income = Income.objects.get(id=codigo)
    income.delete()
    return redirect('/income/')
    
    
def editincome(request, codigo):
    income = Income.objects.get(id=codigo)
    return render(request, "editIncome.html", {"income": income})

def editarincome(request):
    value_income= request.POST['intvalue_income']
    type_income= request.POST['txttype_income']
    detail_income= request.POST['txtdetail_income']
    date_income=request.POST['datedate_income']
    
    income = Income.objects.get(id=id)
    income.value_income = value_income
    income.type_income = type_income
    income.detail_income = detail_income
    income.date_income = date_income
    income.save()
    
    return redirect('/income/')

def spent_view(request):
    spents = Spent.objects.all()
    return render(request, 'spent/register_spent.html', {'spentslist': spents})

def registerspents(request):
    value_spent= request.POST['intvalue_spent']
    detail_spent= request.POST['txtdetail_spent']
    type_spent= request.POST['txttype_spent']
    date_spent=request.POST['datedate_spent']
    
    spent = Spent.objects.create(value_spent= value_spent, type_spent= type_spent, detail_spent= detail_spent, date_spent= date_spent)
    return redirect('/spent/')

def deletespent(request, codigo):
    spent = Spent.objects.get(id=codigo)
    spent.delete()
    return redirect('/spent/')