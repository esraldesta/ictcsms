from django.urls import path
from account.views import *

urlpatterns = [
     path("", login, name="login"),
     path("register/", register, name="register"),
]
