from django.db import models

# Create your models here.
class Add_Category(models.Model):
    cate_name = models.CharField(max_length=100)
    


    def __str__(self):
        return f'{self.cate_name}'