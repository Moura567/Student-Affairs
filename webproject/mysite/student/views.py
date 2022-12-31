from email import message
from multiprocessing import context
from django.http import HttpResponse
import re
from select import select
from sre_parse import State
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from django.db.models import Q
from .models import *
def add(request):
    if request.method == 'POST':
        name= request.POST['name']
        id= request.POST['id']
        gpa= request.POST['gpa']
        lev= request.POST['level']
        date= request.POST['birth']
        depart= request.POST['depart']
        phone= request.POST['phonenumber']
        gender= request.POST['Gender']
        status= request.POST['select']
        new_student = Add(GPA=gpa,
                   student_id=id,
                   name=name,
                   level=lev,
                   department=depart,
                   birthday=date,
                   phonenumber=phone
                   ,gender=gender,
                   State=status)
        new_student.save()
        return redirect('all')
    return render(request, 'student/Add.html',)

def edit(request,id):
    studnet=Add.objects.get(student_id=id)
    if request.method=='POST':
        x=request.POST['btn']
        if x=='Delete':
            student_id=request.POST['id']
            Add.objects.filter(student_id=id).delete()
            return redirect('all')
        else:
            studnet.name=request.POST['name']
            studnet.student_id=request.POST['id']
            studnet.GPA=request.POST['gpa']
            studnet.level=request.POST['level']
            studnet.birthday=request.POST['birth']
            studnet.department=request.POST['depart']
            studnet.phonenumber=request.POST['phonenumber']
            studnet.gender=request.POST['Gender']
            studnet.State=request.POST['select']
            studnet.save()
            return redirect('all')    
    return render(request, 'student/Edit.html',{'student':studnet})

def department(request):
    if request.method == 'POST':
        x= request.POST['name']
        y=  request.POST['id']
        g= request.POST['gpa']
        z= request.POST['level']
        d= request.POST.get('depart')
        f= request.POST['select']
        department_student = Add(GPA=g,
                   student_id=y,
                   name=x,
                   level=z,
                   department=d,State=f)
        department_student.save()
        return redirect('all')
    return render(request, 'student/Department_page.html', )
def allStudents(request):
    search=Add.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search=search.filter(Q(name__icontains=title) 
                                 |Q(student_id__icontains=title)
                                 |Q(State__icontains=title)
                                 |Q(department__icontains=title)
                                 |Q(GPA__icontains=title))
    students={ 'students':search}
    return render(request, 'student/StudentStatus.html',students)

def change(request,id):
    studnet=Add.objects.get(student_id=id)
    if studnet.State=="Active" or studnet.State=="Active":
        Add.objects.filter(student_id=id).update(State="InActive")
    else:    
        Add.objects.filter(student_id=id).update(State="Active")
    return redirect('all')   
 
