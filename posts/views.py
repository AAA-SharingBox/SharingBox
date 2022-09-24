from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ipware import get_client_ip

from .models import Post
from .forms import PostForm
from good.models import Good

# Create your views here.

def top(request):
    context = []
    posts = Post.objects.all().order_by('created_at').reverse()
    if request.user.is_authenticated:
        for post in posts:
            if Good.objects.filter(post=post, created_by=request.user).exists():
                context.append({'post':post, 'good':True, 'good_count':post.good_count})
            else:
                context.append({'post':post, 'good':False, 'good_count':post.good_count})
    else:
        for post in posts:
            context.append({'post':post, 'good':False, 'good_count':post.good_count})

    context = {'context':context}
    return render(request, 'posts/top.html', context)

def order_good(request):
    context = []
    posts = Post.objects.all().order_by('good_count').reverse()
    if request.user.is_authenticated:
        for post in posts:
            if Good.objects.filter(post=post, created_by=request.user).exists():
                context.append({'post':post, 'good':True, 'good_count':post.good_count})
            else:
                context.append({'post':post, 'good':False, 'good_count':post.good_count})
    else:
        for post in posts:
            context.append({'post':post, 'good':False, 'good_count':post.good_count})

    context = {'context':context}
    return render(request, 'posts/order_good.html', context)


@login_required
def post_new(request):
    client_ip, is_routable = get_client_ip(request)
    if request.method == 'POST' and client_ip is not None:
        form = PostForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.created_by = request.user
                post.ip_address = client_ip
                post.save()
                return redirect(top)
        else:
            form = PostForm()
            return render(request, 'posts/post_new.html', {'form':form})
    else:
        form = PostForm()
        return render(request, 'posts/post_new.html', {'form':form})