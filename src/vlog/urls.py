from django.urls import re_path

from vlog import views

urlpatterns = [
    re_path(r"^home$",
            views.IndexView.as_view(), name='index'),

    re_path(r"^categories/(?P<slug_category>[\w'-]+[\']*)/$",
            views.CategoryView.as_view(), name='category'),

    re_path(r"^categories/$",
            views.CategoriesView.as_view(), name='categories'),

    re_path(r"^categories/(?P<slug_category>[\w'-]+)/articles/$",
            views.ArticlesView.as_view(), name='articles'),

    re_path(r"^categories/(?P<slug_category>[\w'-]+)/articles/(?P<slug_article>[\w'-]+)/$",
            views.ArticleView.as_view(), name='article'),

    re_path(r"^article/(?P<slug_article>[\w'-]+)/$",
            views.ArticleView.as_view(),name='article_short'),

    re_path(r"^tags/$",
            views.TagsView.as_view(), name='tags'),

    re_path(r"^tags/(?P<slug_tag>[\w'-]+)/$",
            views.TagView.as_view(), name='tag'),
]

