from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import Pastry, Member 

class PastryForm(forms.ModelForm): 

    class Meta: 
        model = Pastry 
        fields = ['name', 'category', 'description', 'price', 'image'] 

class OrderForm(forms.Form): 
    pastry_id = forms.IntegerField() 
    quantity = forms.IntegerField() 

class MemberForm(UserCreationForm): 
    contact_number = forms.CharField(max_length=20) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 

class MemberProfileForm(forms.ModelForm): 
    class Meta: 
        model = Member 
        fields = ['contact_number'] 

class UserForm(forms.ModelForm): 
    class Meta: 
        model = User 
        fields = ['first_name', 'last_name', 'email'] 