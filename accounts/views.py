from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
from SharingBox.libraries import get_postcontext_list

# Create your views here.
@login_required
def mypage(request, id):
    posts = Post.objects.filter(created_by=request.user)
    context_list = get_postcontext_list(request, posts)
    context = {'context':context_list}
    return render(request, 'accounts/mypage.html', context)