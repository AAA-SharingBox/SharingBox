from good.models import Good
from posts.models import Post

def get_postcontext_list(request, posts):
    context = []
    if request.user.is_authenticated:
        for post in posts:
            if Good.objects.filter(post=post, created_by=request.user).exists():
                context.append({'post':post, 'good':True, 'good_count':post.good_count})
            else:
                context.append({'post':post, 'good':False, 'good_count':post.good_count})
    else:
        for post in posts:
            context.append({'post':post, 'good':False, 'good_count':post.good_count})
    return context