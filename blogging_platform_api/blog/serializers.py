from rest_framework import serializers
from .models import Post, Category, Tag
from django.contrib.auth.models import User
# Tag Serialzer Model
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# Category Serialzer Model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Post Serialzer Model
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'published_date', 'created_date']
        read_only_fields = ['author', 'published_date', 'created_date']

    def validate(self, attrs):
        if not attrs.get('title'):
            raise serializers.ValidationError("Title is required.")
        if not attrs.get('content'):
            raise serializers.ValidationError("Content is required.")
        if not attrs.get('author'):
            raise serializers.ValidationError("Author is required.")
        return attrs

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user