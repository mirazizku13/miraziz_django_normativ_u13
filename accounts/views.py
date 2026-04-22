from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from accounts.forms import RegisterForm, LoginForm,User_profileForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('games:game_list')
        return render(request, 'accounts/login.html', {'form': form})
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.method == 'GET':
        form = User_profileForm(instance=request.user)
        return render(request, 'accounts/profile.html', {'form': form})
    elif request.method == 'POST':
        form = User_profileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('games:game_list')
        return render(request, 'accounts/profile.html', {'form': form})
