import uuid
from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key= True)
    idrandom = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, blank = False, null= False)
    location = models.CharField(max_length=100, blank = False, null= False)
    description = models.CharField(max_length=300, blank = False, null= False)
class Devices(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=30, blank = False, null= False)
    location = models.CharField(max_length=100, blank = False, null= False)

class Template(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=30, blank = False, null= False)
    sensor = models.CharField(max_length=50,blank = False, null= False)
    red = models.CharField(max_length=50, blank = False, null= False)  
    descripcion = models.CharField(max_length=100, blank = False, null= False)
# Create your models here.