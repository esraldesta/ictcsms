from django import forms
from django.forms import widgets
from .models import Issue

class IssueCreationForm(forms.ModelForm):
    class Meta:
        model   = Issue
        fields  = ['user','returndate','material']
        widgets ={
         "returndate":forms.DateInput(attrs={"type":'date'}),   
        }