from django.shortcuts import render,redirect
from .import models
from .import form
# Create your views here.
def add_task(request):
    if request.method == "POST":
        Task_form = form.TaskForm(request.POST)
        if Task_form.is_valid():
           Task_form.save()
           return redirect("show")
    else:
       Task_form=form.TaskForm()
    return render(request,'addTask.html',{'task':Task_form})

def edit_task(request,id):
      edit=models.TaskModel.objects.get(pk=id)
      Task_form = form.TaskForm(instance=edit)
      if request.method == "POST":
        Task_form = form.TaskForm(request.POST,instance=edit)
        if Task_form.is_valid():
           Task_form.save()
           return redirect("show")
     
      return render(request,'addTask.html',{'task':Task_form})

def delete_task(request,id):
   task=models.TaskModel.objects.get(pk=id)
   task.delete()
   return redirect('show')