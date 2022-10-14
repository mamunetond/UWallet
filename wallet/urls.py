from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('income/', views.income_view, name = 'register_income'),
    path('registerIncome/', views.registerincomes),
    path('academy/', views.academy),
    path('home/academy', views.academy),
    path('feed/', views.feed),
    path('home/feed', views.feed),
    path('home/academy/QueSonFP', views.QueSonFP),
    path('home/academy/ObjetivosFP', views.ObjetivosFP),
    path('home/academy/ElementosFP', views.ElementosFP),
    path('home/academy/OptimizarFP', views.OptimizarFP),
    path('home/academy/QueSonGH', views.QueSonGH),

]
