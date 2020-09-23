from django import forms
from .models import user 

class UserForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=20)
    password = forms.CharField(min_length=5, max_length=20)
    image = forms.ImageField(required=False)
    otherinfo = forms.CharField(required=False, max_length=500) 
    

