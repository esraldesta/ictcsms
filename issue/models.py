from django.db import models
from account.models import User
from material.models import Material
# Create your models here.

class Issue(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    material       = models.ForeignKey(Material,on_delete=models.CASCADE)
    amount         = models.IntegerField(default=1) 
    created        = models.DateTimeField(auto_now_add=True)
    returndate     = models.DateField(null=True,blank=True)
    returneddate   = models.DateField(null=True,blank=True)
    adminapproval  = models.BooleanField(default=False)
    storeapproval  = models.BooleanField(default=False)
    who            = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.user.username + "------>  " +self.material.name