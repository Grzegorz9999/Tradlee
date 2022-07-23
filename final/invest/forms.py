from django import forms
from django.forms import ModelForm


class AddCompanyForm(forms.Form):
    name = forms.CharField(label='Wpisz nazwę', max_length=64)
    short_name = forms.CharField(label='Wpisz TICKER', max_length=10)
    description = forms.CharField(label='Opis spółki', max_length=1000)
    history = forms.CharField(label='Historia spółki', max_length=1000)

