from django.contrib import admin
from django.db import models
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    date_hierarchy ='start_date'
    list_display = ['user_name','phone_number','is_staff']
    list_filter  = ['role','department']
    search_fields = ['user_name','first_name','last_name']

admin.site.register(User,UserAdmin)