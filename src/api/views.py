from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from vlog.models import Category, Article, Tag


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug')

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug')

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug')

# ViewSets define the view behavior.
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


