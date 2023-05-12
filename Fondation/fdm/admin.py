from django.contrib import admin
from .models import *


# Register your models here.


class AdminOrganigramme(admin.ModelAdmin):
    list_display = ('titre', 'mission')


admin.site.register(Organigramme, AdminOrganigramme)


class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom', 'description')


admin.site.register(Categorie, AdminCategorie)


class AdminEquipe(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'genre', 'fonction', 'phone', 'adhesion', 'photo', 'actif')


admin.site.register(Equipe, AdminEquipe)


class AdminArticle(admin.ModelAdmin):
    list_display = ('titre','texte', 'categorie', 'photo', 'created_at', 'updated_at')


admin.site.register(Article, AdminArticle)



