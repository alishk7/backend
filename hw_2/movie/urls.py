from django.urls import path
from .views import get_movies, get_movie_by_id

urlpatterns = [
    path('', get_movies, name='movies-list'),
]
