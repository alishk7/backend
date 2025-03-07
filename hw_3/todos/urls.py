from django.urls import path
from .views import get_todos, get_todo_by_id, create_todo, delete_todo, todo_list

urlpatterns = [
    path('', get_todos, name='todos-list'),
    path('<int:id>/', get_todo_by_id, name='todo-detail'),
    path('create/', create_todo, name='todo-create'),
    path('<int:id>/delete/', delete_todo, name='todo-delete'),
    path('list/', todo_list, name='todos-page'),
]
