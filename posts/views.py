from django.shortcuts import render, HttpResponse, redirect, reverse
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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.author = request.user
            new_blog_post.save()
            return redirect(reverse('show_posts'))
    else:
        form = PostForm()
        return render(request, 'posts/create.html', {
            'form': form
        })
        
def search_post(request):
    search_terms = request.GET['search_terms']
    Post.objects.filter(title=search_terms)
    