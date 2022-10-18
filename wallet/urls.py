from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('income/', views.income_view, name = 'register_income'),
    path('registerincomes/', views.registerincomes),
    path('academy/', views.academy),
    path('home/academy', views.academy),
    path('feed/', views.feed),
    path('home/feed', views.feed),
    path('home/academy/QueSonFP', views.QueSonFP),
    path('home/academy/ObjetivosFP', views.ObjetivosFP),
    path('home/academy/ElementosFP', views.ElementosFP),
    path('home/academy/OptimizarFP', views.OptimizarFP),
    path('home/academy/QueSonGH', views.QueSonGH),
    path('spent/', views.spent_view, name = 'register_spent'),
    path('income/deleteincome/<codigo>', views.deleteincome),
    path('income/editincome/<codigo>', views.editincome),
    path('editarincome/<codigo>', views.editarincome),
    path('registerspents/', views.registerspents),
    path('spent/deletespent/<codigo>', views.deletespent),
    path('spent/editspent/<codigo>', views.editspent),
    path('editarspent/<codigo>', views.editarspent),
    path('estadis/', views.estadis, name = 'estadis'),
]
