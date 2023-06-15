from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class addbussi(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    category=models.CharField(max_length=25)
    timing_to=models.IntegerField()
    timing_from=models.IntegerField()
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    Timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    url=models.URLField()
    imagelink=models.URLField()

    def __str__(self):
        return ''+self.name

class contact(models.Model):
    sid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    topic=models.CharField(max_length=70)
    message=models.TextField(max_length=100)

    def __str__(self):
        return 'name:'+self.name