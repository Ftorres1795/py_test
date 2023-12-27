from django.db import models

class TaskStatus(models.IntegerChoices):
    ACTIVE = 1, 'Active'
    INACTIVE = 2, 'Inactive'
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=TaskStatus.ACTIVE, choices=TaskStatus.choices)
    user = models.IntegerField(default=1)