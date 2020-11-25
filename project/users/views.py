from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .decorators import unauthenticated_user, allowed_users

# User registration view
@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name="admin").exists() or user.groups.filter(name="librarian").exists():
                return redirect('admin')
            return redirect('landing-home')
    return render(request, 'users/login.html')

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            usernames = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            group = Group.objects.get(name='reader')
            user.groups.add(group)

            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['reader'])
def profile(request):
    return render(request, 'users/profile.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['reader'])
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated successfully!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    return render(request, 'users/profile_edit.html')