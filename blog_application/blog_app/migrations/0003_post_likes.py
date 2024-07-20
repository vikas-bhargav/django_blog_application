# Generated by Django 5.0.7 on 2024-07-20 05:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_update_model_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, help_text='Likes of post.', related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]