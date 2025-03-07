from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.shortcuts import render
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']

def get_todos(request):
    todos = list(Todo.objects.values())
    return JsonResponse(todos, safe=False)


def get_todo_by_id(request, id):
    todo = get_object_or_404(Todo, id=id)
    return JsonResponse({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "due_dates": str(todo.due_date),
        "status": todo.status
    })

@csrf_exempt
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
        return JsonResponse({"error": "Invalid request"}, status=400)
    
@csrf_exempt
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/todos/')

def todo_list(request):
    todos = Todo.objects.all().order_by('due_date')
    return render(request, 'todos/todo_list.html', {'todos': todos})




# Create your views here.
