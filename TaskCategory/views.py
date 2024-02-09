from django.shortcuts import render,redirect
from .import form
from .import models

# Create your views here.
def add_Category(request):
     
    if request.method == "POST":
        Category_form = form.CategoryForm(request.POST)
        if Category_form.is_valid():
           Category_form.save()
           return redirect("show")
    else:
       Category_form=form.CategoryForm()
    
    return render(request,'addcategory.html',{'category':Category_form})

def edit_Category(request,id):
    edit=models.TaskCategory.objects.get(pk=id)
    Category_form = form.CategoryForm(instance=edit)
    if request.method == "POST":
        Category_form = form.CategoryForm(request.POST,instance=edit)
        if Category_form.is_valid():
           Category_form.save()
           return redirect("show")
  
    
    return render(request,'addcategory.html',{'category':Category_form})