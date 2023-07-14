from django.shortcuts import render,redirect
from .models import Student 
# Create your views here.

def home(request):
    std=Student.objects.all()
    return render(request,'revastd/home.html',{'std':std})

def add_students(request):
    if request.method=='POST':
        print("Student Details Added")
        #taking the user inputs 
        std_srn=request.POST.get("std_srn")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")
        std_phone=request.POST.get("std_phone")


#create an object of the class Student in the model we created 
        s=Student()
        s.srn=std_srn
        s.name=std_name
        s.email=std_email
        s.address=std_address
        s.phone=std_phone

        s.save()
        return redirect("/revastd/home/")

    return render(request,'revastd/add_students.html')

def delete_std(request,srn):
    s=Student.objects.get(pk=srn)
    s.delete()

    return redirect("/revastd/home/")


def update_std(request,srn):
    std=Student.objects.get(pk=srn)
    return render(request,'revastd/update_std.html',{'std':std})

def doupdate_std(request,srn):
    std_srn=request.POST.get("std_srn")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_address=request.POST.get("std_address")
    std_phone=request.POST.get("std_phone")

    std=Student.objects.get(pk=srn)

    std.srn=std_srn
    std.name=std_name
    std.email=std_email
    std.address=std_address
    std.phone=std_phone

    std.save()
    return redirect("/revastd/home")