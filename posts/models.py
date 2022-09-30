from django.db import models
from django.conf import settings
import uuid
from django.core.validators import URLValidator #URLのバリデータを設定する関数をインポート

from tags.models import Tag

# Create your models here.
class Post(models.Model):

    #URLのバリデータを作成、許可はhttp, httpsのみ。
    UrlValidator = URLValidator(
        schemes = ('http', 'https')
    )

    #プライマリーキーはどのモデルでもuuidを使用する
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #URLfieldにバリデータを設定するとデフォルトのバリデータへの追加での設定になってしまうので、CharFieldを使用する。
    url = models.CharField('リンク', validators=[UrlValidator], max_length=500) 
    
    search_word = models.CharField('検索したワード', max_length=200)
    description = models.TextField('コメント', blank=True)
    tag = models.ManyToManyField(Tag)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IPアドレス', protocol='both')

    good_count = models.IntegerField('いいね数', default=0)