from models import Student
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    studentlist = Student.objects.all()
    return render_to_response('template.html',{"studentlist":studentlist})
