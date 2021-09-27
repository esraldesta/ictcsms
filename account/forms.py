from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm as Uc
from django.core.exceptions import ValidationError
from .models import User,Department

class UserCreationForm(Uc):
    class Meta:
        model = User
        fields = ['email','user_name','first_name','last_name','phone_number','role','department']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if(self.cleaned_data["role"]=="superadmin"):
            user.is_staff=True
            user.is_superuser=True
        if commit:
            user.save()
        return user

class DepartmentCreationForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class UserChangeForm(forms.ModelForm):
    old_password       = forms.CharField(widget=forms.PasswordInput()) 
    new_password1      = forms.CharField(widget=forms.PasswordInput()) 
    new_password2      = forms.CharField(widget=forms.PasswordInput()) 
    class Meta:
        model = User
        fields = ['email','old_password','new_password1','new_password2']
    
    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.instance.check_password(old_password):
            raise ValidationError('password_incorrect')
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('password_mismatch')
        password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.instance.set_password(password)
        if commit:
            self.instance.save()
        return self.instance
