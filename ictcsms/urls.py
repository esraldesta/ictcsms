
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('account.urls')),
    path("account", include("account.urls")),
    path('admin/', admin.site.urls),
]
