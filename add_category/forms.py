from django import forms
from .import models


class Add_Cate_Form(forms.ModelForm):
    class Meta:
        model = models.Add_Category
        fields = '__all__'
        labels ={
            'cate_name':'Category Name'
        }
        