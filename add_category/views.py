from django.shortcuts import render,redirect
from .import forms
# Create your views here.


def add_category(request):
    if request.method=='POST':
       form = forms.Add_Cate_Form(request.POST)
       if form.is_valid():
          form.save()
          return redirect('home')
    else:
        form = forms.Add_Cate_Form()
    return render(request,'add_category.html',{'form':form})