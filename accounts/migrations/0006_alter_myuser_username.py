# Generated by Django 4.1.1 on 2022-09-29 23:28

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(help_text='5文字以上の英数字', max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator('^[a-zA-Z0-9]*$'), django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='ID'),
        ),
    ]