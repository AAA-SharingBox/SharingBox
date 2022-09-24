from django.shortcuts import render
from django.http import JsonResponse

from good.models import Good
from posts.models import Post

from ipware import get_client_ip

# Create your views here.

def good_change(request, post_id):
    client_ip, is_routable = get_client_ip(request)
    post = Post.objects.get(id=post_id)
    if request.user.is_authenticated and post is not None:
        record = Good.objects.filter(
            post=post,
            created_by=request.user
        )
        if record.exists():
            record.delete()
            post.good_count -= 1
            post.save()
        else:
            new_record = Good(
                post=post,
                created_by=request.user,
                ip_address=client_ip
            )
            new_record.save()
            post.good_count += 1
            post.save()

        data = {
            "status":"OK",
        }
        return JsonResponse(data)
    else:
        data = {
            "status":"NG",
        }
        return JsonResponse(data)