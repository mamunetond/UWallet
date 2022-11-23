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
    
#Base datos Goals

class Goal(models.Model):
    name_goal = models.CharField(max_length=50)
    value_goal = models.IntegerField(default=0)
    date_goal = models.DateField('Goal date.')
    
#Base datos Dues
    
class Due(models.Model):
    name_due = models.CharField(max_length=50)
    number_due = models.IntegerField(default=0)
    date_due = models.DateField('Due date.')
    detail_due = models.DateField(max_length=200)
    
#Base datos Reminders

class Reminder(models.Model):
    name_reminder = models.CharField(max_length=50)
    date_due = models.DateField('Due date.')
    remember_reminder = models.IntegerField(default=0)
    detail_due = models.DateField(max_length=200)
    




    
    
    