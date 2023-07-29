from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recepie(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    rcepie_name=models.CharField(max_length=100)
    recepie_description=models.TextField()
    recpie_image=models.ImageField(upload_to="recepie")

