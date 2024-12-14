from rest_framework import serializers
from .models import Post, Category, Comment

class PostsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'
        # read_only=['category', ]

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = '__all__'
        read_only = ['post',]