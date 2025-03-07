from django.http import JsonResponse
from .models import Article

def get_articles(request):
    articles = list(Article.objects.values())  
    return JsonResponse(articles, safe=False)

def get_article_by_id(request, id):
    try:
        article = Article.objects.values().get(id=id)
        return JsonResponse(article)
    except Article.DoesNotExist:
        return JsonResponse({"error": "Article not found"}, status=404)