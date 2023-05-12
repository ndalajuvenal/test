from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Nom utilisateur', widget=forms.TextInput(attrs={
       'class':'form-control input','autocomplete': 'off','placeholder':'username'
    }))
    password=forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={
       'class':'form-control input','autocomplete': 'off' ,'placeholder':'password'
    }))

class UserForm(UserCreationForm):
          username=forms.CharField(label='Nom utilisateur', widget=forms.TextInput(attrs={
       'class':'form-control input','autocomplete': 'off','placeholder':'username'
    }))
      
          password1=forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={
       'class':'form-control input','autocomplete': 'off' ,'placeholder':'password'
    }))
          password2=forms.CharField(label='Confirmation Mot de passe', widget=forms.PasswordInput(attrs={
       'class':'form-control input','autocomplete': 'off' ,'placeholder':'confirmation mot de passe'
    }))
  
        
          class Meta:
            model=User
            fields=('username','password1','password2')

class ProfileForm(forms.ModelForm):
      birthday=forms.DateField(label='Naissance', widget=forms.DateInput(attrs={
       'class':'form-control input','autocomplete': 'off' ,'placeholder':'date de naissance','type':'date'
    }))
      phone=forms.IntegerField(label='Naissance', widget=forms.TextInput(attrs={
       'class':'form-control input','autocomplete': 'off' ,'placeholder':'phone','type':'number'
    }))
      class Meta:
            model = Profile
            fields=('birthday','phone','photo','genre')
   
    