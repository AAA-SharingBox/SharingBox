# Generated by Django 4.1.1 on 2022-09-29 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
