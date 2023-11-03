from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status='published')  # Filter published posts
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})


# Create your views here.
