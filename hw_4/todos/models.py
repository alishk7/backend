from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    