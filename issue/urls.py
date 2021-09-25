from django.urls import path
from .views import *
app_name="issue"

urlpatterns = [
    path("list",list_issue,name="listissue"),
    path("create",create_issue,name="createissue"),
    path("update<int:pk>",update_issue,name="updateissue"),
    path("delete<int:pk>",delete_issue,name="deleteissue"),
]
