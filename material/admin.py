from django.contrib import admin
from .models import Material,Category
# Register your models here.


class MaterialAdmin(admin.AdminSite):
    site_title  = "MaterialSite"
    site_header = "Material administration"
    index_title = "MaterialAdmin"

admin_site=MaterialAdmin(name="materialadmin")

class MaterialModelAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display   = ['name','amount','serial_no','shelf_no','column_row']
    list_filter    = ['status','lasting']
    search_fields  = ['name','serial_no','pincode']

class CategoryModelAdmin(admin.ModelAdmin):
    search_fields  = ['name','serial_no','pincode']

admin_site.register(Material,MaterialModelAdmin)
admin_site.register(Category,CategoryModelAdmin)