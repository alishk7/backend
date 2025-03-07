from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('threads/', views.thread_list, name='threads'),
    path('threads/<int:id>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:id>/delete/', views.thread_delete, name='thread_delete'),
    path('threads/<int:id>/edit/', views.thread_edit, name='thread_edit'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('threads/create/', views.thread_create, name='thread_create'),
    path('threads/<int:id>/post/create/', views.post_create, name='post_create'),
]