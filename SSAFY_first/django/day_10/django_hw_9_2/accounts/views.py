from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request,'accounts/index.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/index.html',context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html',context)