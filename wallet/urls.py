from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('income/', views.income_view, name = 'register_income'),
    path('registerincomes/', views.registerincomes),
    path('income/deleteincome/<codigo>', views.deleteincome),
    path('income/editincome/<codigo>', views.editincome),
    path('editarincome/<codigo>', views.editarincome),
    path('spent/', views.spent_view, name = 'register_spent'),
    path('registerspents/', views.registerspents),
    path('spent/deletespent/<codigo>', views.deletespent),
    path('spent/editspent/<codigo>', views.editspent),
    path('editarspent/<codigo>', views.editarspent),
    
]
