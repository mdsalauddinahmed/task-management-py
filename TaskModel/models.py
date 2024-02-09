from django.db import models
# from django import forms

# Create your models here.

class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    taskAssignDate = models.DateField()
    is_completed = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.title
