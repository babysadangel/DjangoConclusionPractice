from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from  io import  StringIO
from demo.models import  Subject, Teacher

def show_subjects(request):

    ctx = {'subjects_list': Subject.objects.all()}
    return  render(request, 'subject.html',ctx)

def show_teachers(request, no):

    teachers = Teacher.objects.filter(subject__no=no)
    ctx = {'teachers_list' : teachers}
    return  render(request,'teacher.html',ctx)