from django.shortcuts import render, HttpResponse

# Create your views here.
def show_posts(request):
    return HttpResponse("It's working!")