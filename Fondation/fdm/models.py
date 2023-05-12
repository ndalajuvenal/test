from django.db import models
from datetime import datetime, date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


# Create your models here.

class Organigramme(models.Model):
    titre = models.CharField(max_length=70,default="membre")
    mission = models.CharField(max_length=200)

    class Meta:
        db_table = "Organigramme"

    def __str__(self):
        return self.titre


Genre = [
    ('M', 'Masculin'),
    ('F', 'Feminin'),
]


class Equipe(models.Model):
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70, blank=True, null=True)
    genre = models.CharField(max_length=10, choices=Genre, default='M')
    fonction = models.ForeignKey(Organigramme, on_delete=models.CASCADE)
    phone = models.CharField(max_length=70)
    adhesion = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    photo = models.FileField(blank=True, null=True, upload_to='photo/')
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = "Equipe"

    def __str__(self):
        return self.nom

    @property
    def anciennete(self):
        today = date.today()
        delta = today.year - self.adhesion.year
        return int(delta)


class Categorie(models.Model):
    nom = models.CharField(max_length=70)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "Categorie"

    def __str__(self):
        return self.nom





class Contact(models.Model):
    Emailto = models.CharField(max_length=70)
    EmailFrom = models.CharField(max_length=200)
    subjectText = models.CharField(max_length=70)
    bodyText = models.CharField(max_length=200)

    class Meta:
        db_table = "Contact"

    def __str__(self):
        return self.EmailFrom


class Article(models.Model):
    titre = models.CharField(max_length=70)
    texte = RichTextField(default='')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to='photo/',default='photo/nature.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = "Article"

    def __str__(self):
        return self.titre
