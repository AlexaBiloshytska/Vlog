from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404

from core.views import BaseView
from vlog.models import Category, Tag, Article


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects \
                         .annotate(category_population=Count('articles')) \
                         .order_by('-category_population')[:3]
        context.update({'categories': categories})

        articles = Article.objects \
                       .annotate(article_comments=Count('comments')) \
                       .order_by('-article_comments')[:10]
        context.update({'articles': articles})

        tags = Tag.objects \
                   .annotate(tags_articles=Count('articles')) \
                   .order_by('-tags_articles')[:10]
        context.update({'tags': tags})
        return self.render_to_response(context)


class CategoriesView(BaseView):
    template_name = 'vlog/categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects\
                         .annotate(category_population=Count('articles')) \
                         .order_by('-category_population')
        context.update({'categories': categories})
        return self.render_to_response(context)

class CategoryView(BaseView):
    template_name = 'vlog/category.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = get_object_or_404(Category, slug = kwargs['slug_category'])
        context.update({'category': category})

        categoryId = category.id
        context.update({'id': categoryId})

        articles = Article.objects \
                       .annotate(article_comments=Count('comments')) \
                       .filter(category_id=categoryId) \
                       .order_by('-article_comments')[:2]
        context.update({'articles': articles})

        articlesAll = Article.objects \
                       .annotate(article_comments=Count('comments')) \
                       .filter(category_id=categoryId) \
                       .order_by('-article_comments')
        context.update({'articlesAll': articlesAll})

        return self.render_to_response(context)

class ArticlesView(BaseView):
    template_name = 'vlog/articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = request.GET.get('page')

        category = get_object_or_404(Category, slug = kwargs['slug_category'])
        context.update({'category': category})

        categoryId = category.id

        articlesAll = Article.objects \
                       .annotate(article_comments=Count('comments')) \
                       .filter(category_id=categoryId) \
                       .order_by('-article_comments')

        paginator = Paginator(articlesAll, 3)
        articles = paginator.get_page(page)

        context.update({'articles': articles})

        return self.render_to_response(context)

class ArticleView(BaseView):
    template_name = 'vlog/article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = get_object_or_404(Article, slug=kwargs['slug_article'])
        context.update({'article': article})
        return self.render_to_response(context)

class TagsView(BaseView):
    template_name = 'vlog/tags.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects \
                   .annotate(tags_articles=Count('articles')) \
                   .order_by('-tags_articles')
        context.update({'tags': tags})

        articles = Article.objects.values('tags', 'title', 'slug') \
            .annotate(comments_count=Count('comments')) \
            .order_by('tags', '-comments_count')
        context.update({'articles': articles})

        return self.render_to_response(context)

class TagView(BaseView):
    template_name = 'vlog/tag.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = get_object_or_404(Tag, slug=kwargs['slug_tag'])

        tagId = tag.id

        articles = Article.objects \
            .annotate(comments_count=Count('comments')) \
            .filter(tags = tagId) \
            .select_related('category') \
            .values('tags', 'title', 'category__title', 'category__slug', 'slug') \
            .order_by('-comments_count')
        context.update({'articles': articles})

        return self.render_to_response(context)