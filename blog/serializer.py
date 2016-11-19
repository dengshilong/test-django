from rest_framework import serializers
from .models import Post, Tag, Category, TestTag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)



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

class TestTagSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = TestTag
        fields = ('id', 'title', 'create_time', 'tags',)