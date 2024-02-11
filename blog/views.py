from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html', context)

def blog_single(request):
    return render(request, 'blog/blog-single.html')