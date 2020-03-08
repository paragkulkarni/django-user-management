from django.shortcuts import redirect, render
from django.contrib.auth.forms import authenticate, UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ProfileForm

# Create your views here.


def profileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = ProfileForm()
    return render(request, 'user_management/profile.html', {'form': form})


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/index/')
    else:
        form = UserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})
