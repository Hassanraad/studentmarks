from django.db import models

class register(models.Model):
    name = models.CharField(max_length=20)
    universityID= models.IntegerField()
    department= models.CharField(max_length=20)
    stage = models.IntegerField()
    
