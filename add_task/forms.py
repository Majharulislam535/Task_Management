from django import forms
from .import models


class Add_Task_Form(forms.ModelForm):
    class Meta:
        model = models.Add_Task
        fields = '__all__'
        widgets={
            'task_assign_date': forms.DateInput(attrs={'type': 'date'}),
        }