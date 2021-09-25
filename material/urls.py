from django.urls import path
from .views import *
app_name="material"

urlpatterns = [
    path("listm",list_material,name="listmaterial"),
    path("listc",list_category,name="listcategory"),
    path("createm",create_material,name="creatematerial"),
    path("createc",create_category,name="createcategory"),
    path("updatec<int:pk>",update_category,name="updatecategory"),
    path("updatem<int:pk>",update_material,name="updatematerial"),
    path("deletec<int:pk>",delete_category,name="deletecategory"),
    path("deletem<int:pk>",delete_material,name="deletematerial"),
]
