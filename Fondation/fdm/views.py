import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q


def home(request):
    return render(request, 'fdm/home.html')


# Article
@login_required
def search_article(request):
    search = request.GET.get('search')
    article = Article.objects.filter(Q(titre__icontains=search) |
                                     Q(texte__icontains=search) |
                                     Q(photo__icontains=search))
    context = {
        'article': article
    }

    return render(request, 'fdm/search_article.html', context)


@login_required
def detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'fdm/detail.html', context)


@login_required
def article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "article ajouté avec succès")
            return redirect('article')

    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'fdm/article_add.html', context)


@login_required
def article_delete(request, id):
    article = Article.objects.get(pk=id)
    if article.user == request.user:
        article.delete()
        messages.success(request, "article supprimé avec succès")
    else:
        raise Http404
    return redirect('article')


@login_required
def article_update(request, id):
    article = Article.objects.get(pk=id)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                messages.success(request, "article mis à jour  avec succès")
                return redirect('article')

        else:
            form = ArticleForm(instance=article)
    else:
        raise Http404
    context = {
        'form': form,
        'article': article
    }
    return render(request, 'fdm/article_update.html', context)


@login_required
def article(request):
    article_show = Article.objects.order_by('-id').all()[:4]
    article = Article.objects.order_by('-id').all()
    article_number = article.count()
    message = f'{article_number} '
    if article_number == 1:
        message = f'{article_number} '

    context = {
        'article': article,
        'article_show': article_show,
        'message': message,
    }
    return render(request, 'fdm/article.html', context)


@login_required
def article_all(request):
    article_show = Article.objects.order_by('-id').all()[:3]
    article = Article.objects.order_by('-id').all()
    article_number = article.count()
    message = f'{article_number} '
    if article_number == 1:
        message = f'{article_number} '

    context = {
        'article': article,
        'article_show': article_show,
        'message': message,
    }
    return render(request, 'fdm/article_all.html', context)


def nous(request):
    return render(request, 'fdm/nous.html')


def deconnection(request):
    logout(request)
    return redirect('base')


def base(request):
    return render(request, 'fdm/base.html')


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'connexion reussie')
            return redirect('home')
        else:
            messages.error(request, 'connexion echoue')
    return render(request, 'fdm/home.html')


# Organigramme

def organigramme_form(request):
    if request.method == 'POST':
        form = OrganigrammeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "nouvelle fonction ajoutée avec succès")
            return redirect('article')

    else:
        form = OrganigrammeForm()
    context = {
        'form': form
    }
    return render(request, 'fdm/article_add.html', context)
