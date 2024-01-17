from django.shortcuts import render
from add_task.models import Add_Task

def home(request):

    task=Add_Task.objects.all()
    
    return render(request,'index.html',{'data':task})