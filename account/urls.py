from django.urls import path
from account.views import *

app_name="account"

urlpatterns = [
    # user crud 
    path('userc/',signup_view,name="signup"),
    path('userl/',user_list_view,name="userl"),
    path('useru/<int:pk>',user_update_view,name="useru"),
    path('userd/<int:pk>',user_delete_view,name="userd"),
    # department crud
    path('departmentc/',department_creation_view,name="departmentc"),
    path('departmentl/',department_list_view,name="departmentl"),
    path('departmentu/<int:pk>',department_update_view,name="departmentu"),
    path('departmentd/<int:pk>',department_delete_view,name="departmentd"),

]
