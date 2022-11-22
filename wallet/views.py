
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .templates.income.Income import RegisterIncome
from .models import Income
from .models import Spent
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


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

def QueSonFP(request):
    return render(request, 'academy/QueSonFP.html')

def ObjetivosFP(request):
    return render(request, 'academy/ObjetivosFP.html')

def ElementosFP(request):
    return render(request, 'academy/ElementosFP.html')

def OptimizarFP(request):
    return render(request, 'academy/OptimizarFP.html')

def QueSonGH(request):
    return render(request, 'academy/QueSonGH.html')

def deleteincome(request, codigo):
    income = Income.objects.get(id=codigo)
    income.delete()
    return redirect('/income/')
    
    
def editincome(request, codigo):
    income = Income.objects.get(id=codigo)
    return render(request, "income/editIncome.html", {"income": income})

def editarincome(request,codigo):
    
    value_income= request.POST['intvalue_income']
    type_income= request.POST['txttype_income']
    detail_income= request.POST['txtdetail_income']
    date_income=request.POST['datedate_income']
    income = Income.objects.get(id=codigo)
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

def editspent(request, codigo):
    spent = Spent.objects.get(id=codigo)
    return render(request, "spent/editSpent.html", {"spent": spent})

def editarspent(request,codigo):
    
    value_spent= request.POST['intvalue_spent']
    type_spent= request.POST['txttype_spent']
    detail_spent= request.POST['txtdetail_spent']
    date_spent=request.POST['datedate_spent']
    spent = Spent.objects.get(id=codigo)
    spent.value_spent = value_spent
    spent.type_spent = type_spent
    spent.detail_spent = detail_spent
    spent.date_spent = date_spent
    spent.save()
    return redirect('/spent/')

def estadis (request):
    labels = []
    data = []
    queryset = Income.objects.order_by('-value_income')[:5]
    for x in queryset:
        labels.append(x.type_income)
        data.append(x.value_income)
        
    print (labels)
    print (data)
    return render(request, 'estadis.html', {
        'labels' : labels,
        'data' : data
    })
    
def notifications(request):
    return render(request, 'notifications/notifications.html')

def welcome(request):
    return render(request, 'welcome/welcome.html')

def login(request):
    return render(request,'login/login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup/signup.html', {'form': form})
        
    
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home') #home
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login/login.html', {'form': form, 'msg':msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form':form} )
    

def signout(request):
    logout(request)
    return redirect('/')

def advices(request):
    return render(request,'advices/advices.html')

def reminders(request):
    return render(request,'reminders/reminders.html')

def dues(request):
    return render(request,'dues/dues.html')

def add_Reminder(request):
    return render(request, 'add_Reminder/add_Reminder.html')

def see_Reminder(request):
    return render(request, 'see_Reminder/see_Reminder.html')

            








