from django.db import models
import uuid
# Create your models here.
class Tag(models.Model):

    #プライマリーキーはどのモデルでもuuidを使用する
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('タグ名', max_length=50)