from django.db import models
# Create your models here.


class User(models.Model):
    role = (
        ("admin", "Admin"),
        ("superadmin", "superadmin"),
        ("user", "user"),
    )
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(null=True, blank=True, max_length=150)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=100,choices=role,default='user')

    def __str__(self):
        return self.name