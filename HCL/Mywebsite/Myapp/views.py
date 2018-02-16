from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import DisplayForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Odc1
from django.utils import timezone
from django.contrib.auth import logout


def dashboard(request):
    today = timezone.now()
    return render(request, 'Myapp/home.html', {'today': today})


def my_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/Mysongs/Songselection')
        else:
            # Return an 'invalid login' error message.
            login(request)
    else:
        return render(request, 'Myapp/login.html')


def registration(request):
    if request.method == 'POST':
        form = DisplayForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/Mysongs/Songselection')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = DisplayForm()
    return render(request, 'Myapp/register.html', {'form': form})


def index(request):
    odc1_list = Odc1.objects.all()
    return render(request, 'Myapp/index.html', {'odc1_list': odc1_list})


def custon_logout(request):
        outtime = timezone.now()
        return render(request, 'Myapp/logout.html', {'loggedout': outtime})
