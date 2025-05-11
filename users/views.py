from django.shortcuts import render, redirect
from .forms import CustomRegisterForm, CustomLoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('Dashboard:dashboard')
    else:
        form = CustomRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('Dashboard:dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})
            
def logout(request):
    if request.user.is_authenticated: # more secure
        auth_logout(request)
        return redirect('main:home')
