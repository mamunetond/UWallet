from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('income/', views.income_view, name = 'register_income'),
]