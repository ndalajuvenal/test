from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


class ArticleForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'
    texte=forms.CharField(label='Texte', widget=forms.Textarea(attrs={
       'class':'form-control',
    }))
    class Meta:
        model = Article
        fields = ('titre','texte','categorie','photo')


    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)


class OrganigrammeForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'
    mission=forms.CharField(label='Mission', widget=forms.Textarea(attrs={
       'class':'form-control',
    }))
    titre=forms.CharField(label='Fonction', widget=forms.TextInput(attrs={
       'class':'form-control',
    }))
    class Meta:
        model = Organigramme
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(OrganigrammeForm, self).__init__(*args, **kwargs)        
    
