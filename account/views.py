from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, Account
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .signals import create_profile, save_profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user

@unauthenticated_user
def register(request):
   
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password1)
            login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()

    return render(request, 'account/register.html', {'registration_form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

@unauthenticated_user
def login_view(request):
    
    
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('/')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


@login_required(login_url='login')
def displayProfile(request):

    # profile = Profile.objects.get(id=request.user.id)
    # context = {"profile":profile}

    return render(request, "account/profile.html", {})


@login_required(login_url='login')
def updateProfile(request):
    if request.POST:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('/profile/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "account/editProfile.html", context)
