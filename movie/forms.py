from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            "username":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Username",
                    "max_length":25
                }
            ),
            "email":forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Email",
                    "max_length":40
                }
            ),
            "password1":forms.PasswordInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Password"                    
                }
            ),
            "password2":forms.PasswordInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Confirm password"                  
                }
            ),
        }