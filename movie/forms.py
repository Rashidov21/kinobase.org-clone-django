from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
 
 
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


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ("name", "comment")
        fields = "__all__"
        exclude = ["movie"]
        
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "comment":forms.Textarea(attrs={"class":"form-control", "rows":3}),
        }