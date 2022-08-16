from django import forms
from wallet.models import Income

class RegisterIncome (forms.Form):
    value_income =forms.IntegerField(label='VALUE', min_value=0)
    type_income =forms.CharField(label='DETAILS' , max_length=200)
    detail_income =forms.CharField(label='DETAILS' , max_length=200)
    dare_income = forms.DateField(label= 'DATE')