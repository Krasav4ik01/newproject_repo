from .models import *
from django.forms import EmailInput, ModelForm, NumberInput, TextInput, DateTimeInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegiterUserForm(UserCreationForm):
    first_name = forms.CharField(label='FistName', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='LastName', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'})) 
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 =forms.CharField(label='Password Again', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name','password1', 'password2']
        

    


class NewsForm(ModelForm, forms.Form):
     class Meta:
        model = Login
        
        fields = ['name', 'surname', 'age', 'username', 'number', 'email', 'password', 'city']
        
        # widgets ={
        #         "number": forms.IntegerField(min_value=10000)
       
        # }




# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class CreateUserForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    
   
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeHolder': ' name of post'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeHolder': ' Anons'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeHolder': ' Text'

            }),
        }


class MvideoForm(ModelForm):
    class Meta:
        model=Mvideo
        fields='__all__'


class CreateUserForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    
   
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        

class ContactForm(forms.Form):
    subject=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"rows": 5}))
    
