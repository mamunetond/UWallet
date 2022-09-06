from django import forms
from wallet.models import Spent

class RegisterSpent (forms.Form):
    value_spent =forms.IntegerField(label='VALUE', min_value=0)
    detail_spent =forms.CharField(label='DETAILS' , max_length=200)
    type_spent =forms.CharField(label='DETAILS' , max_length=200)
    date_spent = forms.DateField(label= 'DATE')