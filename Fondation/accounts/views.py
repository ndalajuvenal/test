from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from .form import UserForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import *

# Create your views here.

def Register(request):
    if request.user.is_authenticated:
        return render(request, 'fdm/home.html')
    if request.method=='POST':
        form=UserForm(request.POST)
        profile_form=ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user=form.save(commit=False)
            profile=profile_form.save(commit=False)
            profile.user=user
            user.save()
            profile.save()
            
    else:
        form=UserForm()  
        profile_form=ProfileForm()    
    context={
        'form':form,
        'profile':profile_form
    }      
    return render(request, 'accounts/register.html',context)

@login_required
def profile_update(request,id):
       profile = Profile.objects.get(pk=id)
       if profile.user == request.user:
        if request.method=='POST':
         form=ProfileForm(request.POST, request.FILES, instance=profile)
         if form.is_valid():
            form.save()
            messages.success(request,"profile mis à jour  avec succès")
            return redirect('home')
         
        else:
          form=ProfileForm(instance=profile)   
       else:
           raise Http404
       context = {
        'form':form,
         'profile':profile
    }
       return render(request, 'accounts/profile_update.html',context)





    
