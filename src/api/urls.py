from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet
from api.views import ArticleViewSet
from api.views import TagsViewSet

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'tags', TagsViewSet)
urlpatterns += router.urls