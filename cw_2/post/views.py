from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author']

# GET
def get_posts(request):
    posts = list(Post.objects.values())
    return JsonResponse(posts, safe=False)

# GET
def get_post_by_id(request, id):
    post = get_object_or_404(Post, id=id)
    return JsonResponse({
        "id": post.id,
        "title": post.title,
        "description": post.description,
        "author": post.author
    })

# POST
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')  # Перенаправление после создания
    else:
        form = PostForm()
    return JsonResponse({"error": "Invalid request"}, status=400)

# DELETE
@csrf_exempt
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('/posts/')

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

# Create your views here.
