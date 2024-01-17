from django.db import models
from add_category.models import Add_Category
# Create your models here.

class Add_Task(models.Model):
    task_title = models.CharField(max_length=150)
    task_description = models.TextField()
    task_assign_date = models.DateField()
    Category = models.ManyToManyField(Add_Category)
    complete = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.task_title}'