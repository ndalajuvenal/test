from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('home', views.home, name='home'),
    path('login', views.connexion, name='login'),
    path('logout', views.deconnection, name='logout'),
    path('nous', views.nous, name='nous'), 
    path('article', views.article, name='article'),
    path('article_all', views.article_all, name='article_all'),
    path('article_add', views.article_form, name='article_add'),
   
    path('detail/<int:id>/', views.detail, name='detail'),
    path('ArticleDelete/<int:id>/', views.article_delete, name='Article_delete'),
    path('Article_update/<int:id>/', views.article_update, name='Article_update'),
    path('search_article/', views.search_article, name='search_article'),
]
