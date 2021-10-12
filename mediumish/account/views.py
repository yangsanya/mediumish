from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm

def login_page(request):
    page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exists')
    return render(request, 'account/login.html')


def logoutUser(request):
    logout(request)

    return redirect('home')


def register_page(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'account/register.html', {'form': form, })


@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    form = UserEditForm(instance=user)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('get_author', pk=user.id)
    return render(request, 'account/edit_profile.html', {'form': form})
