# Generated by Django 4.1.1 on 2022-09-23 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_myuser_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(default='nickname', max_length=10, verbose_name='名前'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator('^[a-zA-Z0-9]*$')], verbose_name='ID'),
        ),
    ]