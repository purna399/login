from django.db import models
from django.contrib.auth.models import User

class EmpPersonal(models.Model):
    name      = models.CharField(max_length=20)
    mobile    = models.CharField(max_length=10)
    per_email = models.CharField(max_length=30)
    age       = models.IntegerField()
    address   = models.TextField()
    country   = models.CharField(max_length=10)
    otp       = models.CharField(max_length=6,default='000000') 
    user      = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    profile_pic = models.FileField(upload_to="media",default='')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'personal_info'


