from django.shortcuts import render,redirect
from .models import Issue
from .forms import *
# Create your views here.

def list_issue(request):
    issues=Issue.objects.all()
    context={
        "issues":issues
    }
    return render(request,"issue/list.html",context)

def create_issue(request):
    if(request.method=="POST"):
        form= IssueCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("issue:listissue")
    else:
        form = IssueCreationForm()
    context={
        "form":form
    }
    return render(request,"issue/create.html",context)

def update_issue(request,pk):
    issue = Issue.objects.get(pk=pk)
    if(request.method=="POST"):
        form= IssueCreationForm(request.POST,instance=issue)    
        if form.is_valid():
            form.save()
            return redirect("issue:listissue")
    else:
        form= IssueCreationForm(instance=issue)

    context={
        "form":form
    }
    return render(request,"issue/create.html",context)

def delete_issue(request,pk):
    issue = Issue.objects.get(pk=pk)
    issue.delete()
    return redirect("issue:listissue")
