# Generated by Django 4.1.1 on 2022-09-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='誕生日'),
        ),
    ]