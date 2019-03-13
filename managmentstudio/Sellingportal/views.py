from django.shortcuts import render
from django.http import HttpResponse
from Sellingportal import models
def Index(request):
    context={'name':'taoufiq',
             'age':30,
             'jobs':['eng','dev', 'lecture']
             }

    return render(request,'index.html',context)

def Student(request):
    students=models.Student.objects.all()
    context={
        'students':students
    }
    return render(request,'students.html',context)


def StudentDegree(request,student_id):
    degrees = models.Degree.objects.filter()
    context = {
        'degrees': degrees
    }
    return render(request, 'degrees.html', context)

