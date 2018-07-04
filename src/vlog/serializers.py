from rest_framework import serializers
from .models import Article, Category, Tag

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug', 'author')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug')