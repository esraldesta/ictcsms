
from django.contrib import admin
from django.urls import path,include
from material.admin import admin_site as materialadmin
from issue.admin import admin_site as issueadmin
from django.urls import path, include

urlpatterns = [
    path("", include('account.urls')),
    path("account", include("account.urls")),
    path("account/",include("account.urls")),
    path("material/",include("material.urls")),
    path("issue/",include("issue.urls")),
    path('admin/', admin.site.urls),
    path('materialadmin/',materialadmin.urls),
    path('issueadmin/',issueadmin.urls),
]
