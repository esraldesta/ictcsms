from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager'

class IctcsmsAdminConfig(AdminConfig):
    default_site = 'manager.admin.Ictcsms'