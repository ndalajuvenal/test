from django.urls import path
from django.contrib.auth import views as auth_views
from .form import LoginForm
from . import views
app_name='accounts'

urlpatterns = [
    path('register/',views.Register, name='register'),
    path('profile_update/<int:id>/',views.profile_update, name='profile_update'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html', next_page='accounts:login'), name='logout'),
]
