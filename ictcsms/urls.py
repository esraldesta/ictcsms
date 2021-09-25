
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path("", include('account.urls')),
    path("account", include("account.urls")),
=======
    path("account/",include("account.urls")),
    path("material/",include("material.urls")),
    path("issue/",include("issue.urls")),
>>>>>>> fd9343d6a8cd5b085b5eb3feb03a360425882c9b
    path('admin/', admin.site.urls),
]
