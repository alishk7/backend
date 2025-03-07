from django.http import JsonResponse
from .models import Movie

def get_movies(request):
    movies = list(Movie.objects.values())  
    return JsonResponse(movies, safe=False)

def get_movie_by_id(request, id):
    try:
        movie = Movie.objects.values().get(id=id)
        return JsonResponse(movie)
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Movie not found"}, status=404)

# Create your views here.
