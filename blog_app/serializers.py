from rest_framework import serializers
from .models import Author, Category, Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'avatar')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'logo')

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'text', 'author', 'category', 'likes', 'views')