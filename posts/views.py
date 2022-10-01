from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ipware import get_client_ip
import re

from .models import Post
from .forms import PostForm

from tags.models import Tag
from SharingBox.libraries import get_postcontext_list

# Create your views here.
def top(request):
    posts = Post.objects.all().order_by('created_at').reverse()
    context_list = get_postcontext_list(request, posts)
    context = {'context':context_list}
    return render(request, 'posts/top.html', context)

def order_good(request):
    posts = Post.objects.all().order_by('good_count').reverse()
    context_list = get_postcontext_list(request, posts)
    context = {'context':context_list}
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
                description = post.description
                tags = re.findall(r"#[^#\s]*", description)
                for tag_str in tags:
                    tag = Tag(name=tag_str)
                    tag.save()
                    post.tag.add(tag)
                return redirect(top)
        else:
            form = PostForm()
            return render(request, 'posts/post_new.html', {'form':form})
    else:
        form = PostForm()
        return render(request, 'posts/post_new.html', {'form':form})