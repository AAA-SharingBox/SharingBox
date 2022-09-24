from django.db import models
from django.conf import settings
import uuid

from  posts.models import Post
# Create your models here.

class Good(models.Model):
    
    #プライマリーキーはどのモデルでもuuidを使用する
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, verbose_name='投稿', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='いいねした人', on_delete=models.CASCADE)
    created_at = models.DateTimeField('いいねした日時', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IPアドレス', protocol='both')