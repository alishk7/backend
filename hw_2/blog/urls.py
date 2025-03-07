from django.urls import path
from .views import get_articles, get_article_by_id

urlpatterns = [
    path('', get_articles, name='articles-list'),
    
]