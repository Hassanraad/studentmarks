from django.db import models
from .utlas import user_directory_path
# Create your models here.
class student(models.Model):
    studentID = models.IntegerField(primary_key=True,unique=True)
    fname = models.CharField(max_length = 25)
    lname= models.CharField(max_length = 25)
    email= models.CharField(max_length = 100)
    academic_year=models.CharField(max_length = 100,default="")
    stage= models.IntegerField(null=True,default=1)
    def __str__(self):
        return self.fname


class subject(models.Model):
    subjects1 = models.CharField(max_length=100 ,default="")
    subjects2 = models.CharField(max_length=100,default="")
    subjects3 = models.CharField(max_length=100,default="")
    subjects4 = models.CharField(max_length=100,default="")
    def __str__(self):
         return str(self.subjects1) 
    
class stage(models.Model):
    stages = models.IntegerField()
    department = models.CharField(max_length=25)
    studentID= models.IntegerField()
    
    def __str__(self):
         return str(self.department)

class grade(models.Model):
    student_id=models.IntegerField()
    fname=models.CharField(max_length=25)
    grades=models.CharField(max_length=255)
    subjects=models.CharField(max_length=255)
    stage=models.IntegerField(null=True)
    def __str__(self):
         return str(self.student_id)

class Profiles(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    email=models.EmailField()
    photo=models.ImageField(upload_to=user_directory_path,null=True ,blank=True)
    department=models.CharField(max_length=100,blank=False)
    

    def __str__(self):
        return f'{self.name}\'s Profiles'