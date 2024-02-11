from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from blog.forms import CommentForm
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
    return render(request, 'blog/blog-single.html',context)

'''def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submitted')
        else:
            messages.add_message(request, messages.ERROR, 'your comment did not submitted')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
   if not post.login_require:
        comments = Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
        print(post.id)  # Verify the post ID value
        context = {'post': post, 'comments': comments, 'form': form}
        return render(request, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))'''