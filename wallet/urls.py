from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('income/', views.income_view, name = 'register_income'),
    path('registerIncome/', views.registerincomes),
]
