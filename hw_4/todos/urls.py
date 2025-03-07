from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('todo-lists/', todo_list_view, name='todo-list'),
    path('todo-lists/<int:id>/', todo_list_detail, name='todo-list-detail'),
    path('todo-lists/create', create_todo_list, name='todo-list-create'),
    path('todo-lists/<int:id>/delete/', delete_todo_list, name='todo-list-delete'),
    path('todo-lists/<int:id>/edit/', edit_todo_list, name='todo-list-edit'),
    path('todo-lists/<int:id>/create_todo/', create_todo, name='todo-create'),
    path('todos/<int:id>/delete/', delete_todo, name='todo-delete'),
]