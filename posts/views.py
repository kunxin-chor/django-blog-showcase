from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def show_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        'posts':posts
    })