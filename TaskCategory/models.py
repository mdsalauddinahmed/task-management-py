from django.db import models

from TaskModel.models import TaskModel
# Create your models here.

class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=50)
    tasks = models.ManyToManyField(TaskModel)

    def __str__(self) -> str:
        return self.categoryName