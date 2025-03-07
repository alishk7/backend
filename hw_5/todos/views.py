from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Todo
from .forms import TodoForm

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=400)
    return render(request, 'todos/login.html')

@csrf_exempt
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"message": "Logged out"}, status=200)
    return JsonResponse({"error": "User not logged in"}, status=400)

@login_required
def get_todos(request):
    todos = Todo.objects.filter(user=request.user).values()
    return JsonResponse(list(todos), safe=False)

@login_required
def get_todo_by_id(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return JsonResponse({
        "title": todo.title,
        "description": todo.description,
        "due_date": todo.due_date.strftime("%Y-%m-%d"),
        "status": todo.status
    })

@csrf_exempt
@login_required
def create_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        todo = Todo.objects.create(
            title=data.get("title"),
            description=data.get("description"),
            due_date=data.get("due_date"),
            status=data.get("status", False),
            user=request.user
        )
        return JsonResponse({"message": "Todo created", "id": todo.id}, status=201)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
@login_required
def delete_todo(request, todo_id):
    if request.method == "DELETE":
        todo = get_object_or_404(Todo, id=todo_id, user=request.user)
        todo.delete()
        return JsonResponse({"message": "Todo deleted"}, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)



@login_required
def todos_list_view(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todos.html', {'todos': todos})

@login_required
def create_todo_view(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})

@login_required
def delete_todo_view(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('todos_list')
    return render(request, 'todos/delete_confirm.html', {'todo': todo})



