from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
def hp(request):
    ac=students.objects.all()
    template=loader.get_template('app1/stu.html')
    return HttpResponse(template.render(request))

def detial(request,prostu_id):
    return HttpResponse('<h2>Student Detials for student_id :' +str(prostu_id)+'</h2>')