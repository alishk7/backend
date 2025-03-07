from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoListForm, TodoForm
from .models import TodoList, Todo

def home(request):
    return redirect('/todo-lists/')

def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_list.html', {'todo_lists': todo_lists})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    return render(request, '/todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

@csrf_exempt
def create_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo-lists/')
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('/todo-lists/')

@csrf_exempt
def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form  = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect(f'/todo-lists/{id}')
    return render(request, 'todos/todo_list_edit.html', {'todo_list': todo_list})

@csrf_exempt
def create_todo(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect(f'/todo-lists/{id}')
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect(f'/todo-lists/{todo_list_id}')


