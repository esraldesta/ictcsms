from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, IntegerField

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    statuschoices=(
        (1,"new"),
        (2,"to be fixed"),
        (3,"wasted"),
    )
    lastingchoices=(
<<<<<<< HEAD
        (1,"new"),
        (2,"to be fixed"),
        (3,"wasted"),
=======
        (1,"fixed"),
        (2,"consumable"),
>>>>>>> fd9343d6a8cd5b085b5eb3feb03a360425882c9b
    )
    name       = models.CharField(max_length=255)
    serial_no  = models.CharField(max_length=255,unique=True,blank=True,null=True)
    pincode    = models.CharField(max_length=255,unique=True,blank=True,null=True)
    amount     = models.IntegerField()
    created    = models.DateField(auto_now_add=True)
    status     = models.IntegerField(choices=statuschoices,default=statuschoices[0][0])
    lasting    = models.IntegerField(choices=lastingchoices,default=lastingchoices[0][0])
    shelf_no   = models.IntegerField(null=True,blank=True)
    column_row = models.IntegerField(null=True,blank=True)
    category   = models.ForeignKey("Category", on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name