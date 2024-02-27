from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=kwargs['tag_name'])
    posts = Paginator(posts,3)
    try:
       page_number = request.GET.get('page')
       posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage :
        posts= posts.get_page(1)
    context={'posts': posts}
    return render(request, 'blog/blog-home.html',context)
def blog_single(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted.')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment could not be submitted.')

    # Retrieve all posts, including the newly created ones
    posts = Post.objects.filter(status=1)

    # Retrieve the newly created post
    new_post = Post.objects.filter(status=1).order_by('-published_date').first()

    comments = Comment.objects.filter(post__in=posts, approved=True)
    form = CommentForm()
    context = {'posts': posts, 'comments': comments, 'form': form, 'new_post': new_post}
    return render(request, 'blog/blog-single.html', context)