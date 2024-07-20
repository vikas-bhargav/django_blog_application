from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model"""
    class Meta:
        """Meta information for the Comment"""
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model"""
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        """Meta information for the Post"""
        model = Post
        fields = ["id", "number_of_likes", "title", "author", "content", "comments", "published_date"]


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""
    password = serializers.CharField(write_only=True)

    class Meta:
        """Meta information for the User"""
        model = User
        fields = ('username', 'email', 'password')
