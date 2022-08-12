from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddCompanyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=64)
    short_name = forms.CharField(label='TICKER', max_length=10)
    stock = forms.CharField(label='Stock', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    history = forms.CharField(widget=forms.Textarea)

class AddIndicatorForm(forms.Form):
    name = forms.CharField(label='Name', max_length=64)
    short_name = forms.CharField(label='Short name', max_length=10)
    definition = forms.CharField(widget=forms.Textarea)

class MyLoginForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class SubscriptionForm(forms.Form):
    email = forms.EmailField(label='', max_length=254)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']