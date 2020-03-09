from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import authenticate, UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ProfileForm, OwnerForm, StoreForm
from .models import Owner, Store

# Create your views here.


def profileView(request):
    if request.method == 'POST':
        ProfileFormIn = ProfileForm(request.POST)
        OwnerFormIn = OwnerForm(request.POST)
        StoreFormIn = StoreForm(request.POST)

        if ProfileFormIn.is_valid():
            ProfileFormIn.save()
            return HttpResponse('success profile form')
        elif OwnerFormIn.is_valid():
            OwnerFormIn.save()
            return HttpResponse('success ownerform form')
        elif StoreFormIn.is_valid():
            StoreFormIn.save()
            return HttpResponse('success storeform form')
    else:
        ProfileFormIn = ProfileForm()
        OwnerFormIn = OwnerForm()
        StoreFormIn = StoreForm()
        ownerdata = Store.objects.all()
        print(ownerdata)
    return render(request, 'user_management/profile.html', {'profile_form': ProfileFormIn, 'owner_form': OwnerFormIn, 'store_form': StoreFormIn, 'ownerdata': ownerdata, })


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
