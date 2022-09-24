from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
@login_required
def mypage(request, id):
    posts = Post.objects.filter(created_by=request.user)
    context = {'posts':posts}
    return render(request, 'accounts/mypage.html', context)