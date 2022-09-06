from django.db import models

# Create your models here.
#Base datos Ingreso
class Income (models.Model):
    value_income = models.IntegerField(default=0)
    type_income = models.CharField(default= "", max_length=200)
    detail_income = models.CharField(max_length=200)
    date_income = models.DateField('Income date.')
    
    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.type_income, self.value_income)
    
#Base datos Gastos
class Spent (models.Model):
    value_spent = models.IntegerField(default=0)
    type_spent = models.CharField(default= "", max_length=200)
    detail_spent = models.CharField(max_length=200)
    date_spent = models.DateField('Spent date.')
    
    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.type_spent, self.value_spent)
    
