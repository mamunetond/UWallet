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

]
