from django.shortcuts import render
from TaskCategory.models import TaskCategory

def home(request):
    return render(request,'home.html')

def show(request):
    data=TaskCategory.objects.all()
    return render(request,'showTask.html',{'data':data})