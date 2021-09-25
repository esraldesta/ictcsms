from django import forms
from django.forms import widgets
from .models import ( Material,Category )

class MaterialCreationForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = "__all__"
        widgets ={
            'shelf_no':forms.NumberInput(attrs={"min":0}),
            'column_row':forms.NumberInput(attrs={"min":0}),
            'amount':forms.NumberInput(attrs={"min":0})
        }
class CatagoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        