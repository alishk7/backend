from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm


def home(request):
    return redirect('threads')


def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'threads_list.html', {'threads': threads})


def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=thread.id)
    else:
        post_form = PostForm()
    return render(request, 'thread_detail.html', {'thread': thread, 'posts': posts, 'post_form': post_form})


def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('threads')


def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'thread_edit.html', {'form': form, 'thread': thread})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'post': post})
def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('threads') 
    else:
        form = ThreadForm()
    return render(request, 'thread_create.html', {'form': form})

def post_create(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread  # Связываем пост с текущим тредом
            post.save()
            return redirect('thread_detail', id=thread.id)  # Перенаправление на страницу треда
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form, 'thread': thread})