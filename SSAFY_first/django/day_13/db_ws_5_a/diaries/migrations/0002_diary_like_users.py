# Generated by Django 4.2.9 on 2024-10-20 08:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='like_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
