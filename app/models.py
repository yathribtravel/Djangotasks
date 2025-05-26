from django.db import models

# Create your models here.

class test(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    
