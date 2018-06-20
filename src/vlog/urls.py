from django.conf.urls import url
from django.urls import path

from vlog import views

urlpatterns = [
    path('home', views.IndexView.as_view(), name='index'),
    path('categories', views.CategoriesView.as_view(), name='categories'),

    url(r'^categories/(?P<slug_category>[\w-]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^categories/(?P<slug_category>[\w-]+)/articles/$', views.ArticlesView.as_view(), name='articles'),
    url(r'^categories/(?P<slug_category>[\w-]+)/articles/(?P<slug_article>[\w-]+)/$',
        views.ArticleView.as_view(), name='article'),

    path('tags', views.TagsView.as_view(), name='tags'),
    url(r'^tags/(?P<slug_tag>[\w-]+)/$', views.TagView.as_view(), name='articles'),

]