from django.contrib import admin
from .models import Issue
# Register your models here.


class IssueAdmin(admin.AdminSite):
    site_title  = "IssueSite"
    site_header = "Issue administration"
    index_title = "IssueAdmin"

admin_site=IssueAdmin(name="issueadmin")

class IssueModelAdmin(admin.ModelAdmin):
    date_hierarchy = "returndate"
    list_display   = ['user','material','amount']
    list_filter    = ['created','adminapproval','storeapproval']
    search_fields  = ['name','serial_no','pincode']

admin_site.register(Issue,IssueModelAdmin)