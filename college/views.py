from django.shortcuts import redirect, render
from .models import Profiles
import uuid
from django.contrib import messages
from .models import student,subject,stage,grade
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
@requires_csrf_token


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('Email')
            password = request.POST.get('Paasword')
            print("Email:", email)
            print("Password:", password)
            profile_exists = Profiles.objects.filter(email=email, password=password).exists()
            print("Queryset Exists:", profile_exists)
            print("Queryset Exists:", Profiles.objects.filter(email=email, password=password).exists())
            if Profiles.objects.filter(email=email, password=password).exists():
                return redirect('marks')
            else:
                messages.error(request, 'You entered an incorrect password or email')
        except Exception as e:
            # Log or print the error
            print("Error during login:", e)
            # Optionally, you can add a message here too
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('login')  # Handle error with a redirect

    return render(request, "college/login.html")
def signup(request):
    if request.method == 'POST':
        try:
            # Generate a unique ID using Django's UUID field
            unique_id = uuid.uuid4()

            # Get form data
            name = request.POST.get('name1')
            password = request.POST.get('password')
            email = request.POST.get('email')
            department = request.POST.get('department')

            if Profiles.objects.filter(email=email):
                messages.error(request, 'This email is already exists')
                
            else:
                # Create Profile instance and save
                profile = Profiles.objects.create(
                    id=unique_id,
                    name=name,
                    password=password,
                    email=email,
                    department=department
                )
                return redirect('login')

            # Redirect to a success page or display a success message
            return render(request, "signup_success.html", {'profile': profile})

        except Exception as e:
            # Log or print the error
            print("Error saving profile:", e)
            # You can also return an error page or message here

    return render(request, "college/slider.html")






def marks(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    studentID =request.POST.get('id')
    department=request.POST.get('dep')
    stage_value = request.POST.get('stage')
    academicYear = request.POST.get('acdyear')
    email=request.POST.get('email')


    
    if request.method == "POST" :
     student_instance =student.objects.create(academic_year=academicYear,fname=fname,lname=lname,email=email,studentID=studentID,stage=stage_value)
     student_instance.save()     
     
     stage_instance=stage.objects.create(department=department,stages=stage_value,studentID=studentID)
     stage_instance.save()
     

    return render(request,'college/home.html')

@requires_csrf_token
def subjects(request):
   if request.method == "POST" :
    subjects1 = request.POST.getlist('subjects1[]')
    subjects2 = request.POST.getlist('subjects2[]')
    subjects3 = request.POST.getlist('subjects3[]')
    subjects4 = request.POST.getlist('subjects4[]')
    getcheck = request.POST.get("checked")
    if getcheck=="yes":
     subject.objects.all().delete()
     grade.objects.all().delete()

    array1=[]
    array2=[]
    array3=[]
    array4=[]
    for s1 in subjects1:
      array1.append(s1)
      
    for s2 in subjects2:
      array2.append(s2)
    for s3 in subjects3:
     array3.append(s3)
    for s4 in subjects4:
      array4.append(s4)
    print(array1)
    
    subject_instance=subject.objects.create(subjects1=array1,subjects2=array2,subjects3=array3,subjects4=array4)
    subject_instance.save()
   return render(request,'college/subjects.html')



@requires_csrf_token
def show(request):
   
     subjects_list=[]
     student_filter=[]
     enteredstage=None
     if request.method == "POST" :
      enteredstagee=request.POST.get('enteredstage')
      enteredstage=enteredstagee
   
     grades_id=[]
     student_grades=grade.objects.all()
     for id in student_grades:
       grades_id.append(id.student_id)
     student_show=student.objects.all()
     stage_show=stage.objects.all()
     
     if enteredstage is not None and enteredstage.isdigit() :
      
      student_filter=student.objects.filter(stage=enteredstage).exclude(studentID__in = grades_id)
      
     subject_instance=subject.objects.first()
     if enteredstage is not None and enteredstage.isdigit():
      enteredstage=int(enteredstage)
     if enteredstage==1:

      subjects_list.extend(eval(subject_instance.subjects1))
     elif enteredstage==2:
       subjects_list.extend(eval(subject_instance.subjects2))
     elif enteredstage==3:
       subjects_list.extend(eval(subject_instance.subjects3))
     elif enteredstage==4:
       subjects_list.extend(eval(subject_instance.subjects4))
     elif enteredstage =="":
       subjects_list.append("")
     else:
       subjects_list=[]


     for n in student_filter:
        id= n.studentID
        for s in subjects_list:
          grades_dict = request.POST.get(f'grades[{id}][{s}]')
          if grades_dict is not None:
           q= grade.objects.create(student_id=id,fname=n.fname,subjects=s,grades=grades_dict,stage=enteredstage)
           q.save()
     filter_id=[] 


     for id in student_filter:
       filter_id.append(id.studentID)
      

     return render(request,'college/show.html',{'students':student_show,'stages':stage_show,"studentFilter":student_filter,"subjectList":subjects_list,"enteredstage":enteredstage})
  

@requires_csrf_token
def grades(request):
  thegrade1 = ""
  studentID1 = ""
  subname1 = ""

  thegrade= request.POST.get('grade1')
  if thegrade is not None and thegrade  !="":
    thegrade1=thegrade
  subname = request.POST.get('subname1')
  if subname is not None and subname  !="":
    subname1 = subname
  studentID =request.POST.get('studentID1')

  print(thegrade)
  grade.objects.filter(student_id=studentID, subjects = subname).update(grades =thegrade)
  




  uniID1=set()
  uniID2=set()
  uniID3=set()
  uniID4=set()
  
  

  s1=[]
  s2=[]
  s3=[]
  s4=[]
  grades1=grade.objects.filter(stage=1)
  grades2=grade.objects.filter(stage=2)
  grades3=grade.objects.filter(stage=3)
  grades4=grade.objects.filter(stage=4)
  subject_instance=subject.objects.first()
  s1.extend(eval(subject_instance.subjects1))
  s2.extend(eval(subject_instance.subjects2))
  s3.extend(eval(subject_instance.subjects3))
  s4.extend(eval(subject_instance.subjects4))
  for obj in grades1:
    uniID1.add(obj.student_id)

  for obj in grades1:
    uniID1.add(obj.student_id)

  for obj in grades2:
    uniID2.add(obj.student_id)
    
  for obj in grades3:
      uniID3.add(obj.student_id)  

  for obj in grades4:
    uniID4.add(obj.student_id)        
  names=[]
  ids=[]
  names2=[]
  ids2=[]
  names3=[]
  ids3=[]
  names4=[]
  ids4=[]
  for i in uniID1:
    for obj in grades1:
      if i==obj.student_id and obj.fname not in names:
         names.append(obj.fname)

  for i in uniID2:
    for obj in grades2:
      if i==obj.student_id and obj.fname not in names2:
         names2.append(obj.fname)  

  for i in uniID3:
    for obj in grades3:
      if i==obj.student_id and obj.fname not in names3:
         names3.append(obj.fname)                
  for i in uniID4:
    for obj in grades4:
      if i==obj.student_id and obj.fname not in names4:
         names4.append(obj.fname)       

  for i in uniID1:
   ids.append(i)
  zipper1=zip(ids,names)

  for i in uniID2:
   ids2.append(i)
  zipper2=zip(ids2,names2)

  for i in uniID3:
   ids3.append(i)
  zipper3=zip(ids3,names3)

  for i in uniID4:
   ids4.append(i)
  zipper4=zip(ids4,names4)      
  return render(request,"college/grades.html",{"grades1":grades1,"grades2":grades2,"grades3":grades3,"grades4":grades4,
                                               "s1":s1,"s2":s2,"s3":s3,"s4":s4,"ziper":zipper1,"ziper2":zipper2,"ziper3":zipper3,"ziper4":zipper4 })