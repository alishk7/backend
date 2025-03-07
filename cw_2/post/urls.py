from django.urls import path
from .views import get_posts, get_post_by_id, create_post, delete_post, post_list

urlpatterns = [
    path('', get_posts, name='posts-list'),
    path('<int:id>/', get_post_by_id, name='post-detail'),
    path('create/', create_post, name='post-create'),
    path('<int:id>/delete/', delete_post, name='post-delete'),
]

urlpatterns += [
    path('list', post_list, name='posts-page')
]