"""
URL configuration for hw_5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todos.views import (
    login_view, logout_view, get_todos, get_todo_by_id,
    create_todo, delete_todo, todos_list_view, create_todo_view,
    delete_todo_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('todos/', get_todos),
    path('todos/<int:todo_id>/', get_todo_by_id),
    path('todos/create/', create_todo),
    path('todos/delete/<int:todo_id>/', delete_todo),
    path('todos/list/', todos_list_view, name='todos_list'),
    path('todos/create/form/', create_todo_view, name='create_todo_form'),
    path('todos/delete/<int:todo_id>/form/', delete_todo_view, name='delete_todo'),
]
