from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    template_name = 'index.html'
    context = {
        'posts': posts
    }
    return render(request, template_name, context)