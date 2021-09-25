from django.shortcuts import render
from account.models import *
from account.forms import *
# Create your views here.


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        print(request.POST)

    context = {
        "forms": form
    }
    return render(request, 'accounts/login.html', context)


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        print(request.POST)
    context = {
        "forms": form
    }
    return render(request, 'accounts/signup.html', context)