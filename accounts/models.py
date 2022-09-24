from django.db import models
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.validators import ASCIIUsernameValidator
import uuid

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username = username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    username_validator = ASCIIUsernameValidator()

    #プライマリーキーはどのモデルでもuuidを使用する
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    username = models.CharField(verbose_name='ID', max_length=50, unique=True, validators=[MinLengthValidator(5,), RegexValidator(r'^[a-zA-Z0-9]*$',), username_validator], help_text='5文字以上の英数字')
    email = models.EmailField(verbose_name='Email', max_length=50, unique=True)
    nickname = models.CharField(verbose_name='名前', max_length=10)
    date_of_birth = models.DateField(verbose_name="誕生日", blank=True, null=True)
    icon = models.ImageField(verbose_name='プロフィール画像', upload_to="image/", blank=True)
    url = models.URLField(verbose_name='リンク', blank=True, null=True)
    introduction = models.TextField(verbose_name='自己紹介', max_length=300, blank=True)
    date_joined = models.DateTimeField(verbose_name='登録日', auto_now_add=True)
    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username