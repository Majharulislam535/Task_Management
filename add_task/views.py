from django.shortcuts import render,redirect
from .models import Add_Task
from .import forms
# Create your views here.


def add_task(request):

    if request.method=='POST':
       form = forms.Add_Task_Form(request.POST)
       if form.is_valid():
          form.save()
          return redirect('home')
    else:
        form = forms.Add_Task_Form()
    return render(request,'add_task.html',{'form':form})


def edit_task(request,id):
    task = Add_Task.objects.get(pk=id)
    form = forms.Add_Task_Form(instance=task)
    if request.method=='POST':
       form = forms.Add_Task_Form(request.POST,instance=task)
       if form.is_valid():
          form.save()
          return redirect('home')
    
    return render(request,'add_task.html',{'form':form})


def delete_task(request,id):
    task = Add_Task.objects.get(pk=id)
    task.delete()
    return redirect('home')
    