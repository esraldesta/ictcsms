from django.urls.base import reverse_lazy
from account.models import User
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.forms import UserChangeForm as UCF
from django.contrib.auth.forms import PasswordChangeForm as PCF
from django.contrib.auth.views import PasswordChangeView as PCV
from django.views import generic 

# user CRUD

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('account:userl') 
    else:
        form = UserCreationForm()
    context={
        "forms" :form
    }
    return render(request, 'account/login.html', context)

def user_list_view(request):
    users = User.objects.all()
    context={
        "users" :users
    }
    return render(request, 'account/list.html', context)

def user_update_view(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserChangeForm(request.POST,instance=user)
        if(form.is_valid()):
            form.save()
            return redirect('account:userl') 
    else:
        form = UserChangeForm()
    context={
        "forms" :form
    }
    return render(request, 'account/login.html', context)

def user_delete_view(request,pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect("account:userl")


# department CRUD

def department_creation_view(request):
    if request.method == 'POST':
        form = DepartmentCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('account:departmentl') 
    else:
        form = DepartmentCreationForm()
    context={
        "forms" :form
    }
    return render(request, 'account/login.html', context)

def department_list_view(request):
    departments = Department.objects.all()
    context={
        "departments" :departments
    }
    return render(request, 'account/list.html', context)

def department_update_view(request,pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
        form = DepartmentCreationForm(request.POST,instance=department)
        if(form.is_valid()):
            form.save()
        return redirect('account:departmentl') 
    else:
        form = DepartmentCreationForm(instance=department)
    context={
        "forms" :form
    }
    return render(request, 'account/login.html', context)

def department_delete_view(request,pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return redirect("account:departmentl")
