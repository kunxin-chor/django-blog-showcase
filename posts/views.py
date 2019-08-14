from django.shortcuts import render, HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def show_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        'posts':posts
    })
    
def create_post(request):
    if request.method == 'POST':
        # process the from
        pass
    else:
        form = PostForm()
        return render(request, 'posts/create.html', {
            'form': form
        })