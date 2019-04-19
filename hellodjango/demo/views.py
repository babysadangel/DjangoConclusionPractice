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

def make_comment(request, no):
    ctx  ={'code' : 200}

    try:
        teacher = Teacher.objects.get(pk=no)

        if request.path.startswith('/good'):
            teacher.good_count += 1
            ctx['result'] = f'好评({teacher.gcount})'
        else:
            teacher.bad_count += 1
            ctx['result'] = f'差评({teacher.bcount})'

        teacher.save()

    except Teacher.DoesNotExist:
        ctx['code'] = 404

    return  HttpResponse(json.dumps(ctx),
                         content_type='application/json; charset=utf-8')