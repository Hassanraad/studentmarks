from django.shortcuts import render
from .models import register
from . forms import registerForm

def info(request):
    Name = request.POST.get('name')
    UniversityID = request.POST.get('unid')
    department = request.POST.get('dep')
    stage = request.POST.get('stage')
    if request.method == "POST" :
     data= register(name=Name,universityID=UniversityID,department=department,stage=stage).save()
    
    
    
    #data.save()
    return render(request,'students/info.html',{'data':register.objects.all})

