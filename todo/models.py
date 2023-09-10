from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    memo = models.TextField(blank =True)
    created_at = models.DateTimeField(auto_now_add=True)
  #  due_date = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # one to many relationship, one user can have a lot of todos but teh todos can be for only that user

    def __str__(self):
       return self.title
