from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('profiles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('profiles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('profiles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html',context)

def update(request,user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        form = CustomUserChangeForm()
    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        'form': form,
    }
    return render(request,'accounts/update.html',context)