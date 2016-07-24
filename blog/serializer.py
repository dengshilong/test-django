from rest_framework import serializers
from .models import Post, Tag, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'publish_time', 'category', 'tag', )
