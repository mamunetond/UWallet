from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('income/', views.income_view, name = 'register_income'),
    path('registerincomes/', views.registerincomes),
    path('spent/', views.spent_view, name = 'register_spent'),
    path('registerspents/', views.registerspents)
    
]
