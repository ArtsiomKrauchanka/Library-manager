from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            usernames = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            return redirect('landing-home')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
    