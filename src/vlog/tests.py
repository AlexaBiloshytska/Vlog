from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from vlog import models
from vlog import forms
from vlog import views
from core.views import BaseView
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image

class TransliterationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )

    def test_transliteration(self):
        im_io = BytesIO()
        im = Image.new(mode='RGB', size=(200, 200))
        im.save(im_io, 'JPEG')

        cat_form = forms.CategoryForm(
            {
                'title': 'спорт',
                'author': self.user.pk,
                'image': InMemoryUploadedFile(
                    im_io, None, 'random.jpg', 'image/jpeg', len(im_io.getvalue()), None
                )
            }
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'sport')

        cat_form = forms.CategoryForm(
            {'title': 'тест'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'test')

        cat_form = forms.CategoryForm(
            {'title': 'Breaking News! Новости.'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'breaking-news-novosti')

class Test_Vlog(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )
        category = models.Category.objects.create(
            title='спорт',
            slug='sport',
            author=self.user
        )
        self.article = models.Article.objects.create(
            title='Бег по утрам',
            slug='beg-po-utram',
            author=self.user,
            category=category
        )
        models.Tag.objects.create(
            title='бег',
            slug='beh',

        )
        models.Comment.objects.create(
            author=self.user,

        )
        BaseView(template_name = 'example.tpl')
        views.Category.objects.create(
            title='пример',
            slug='primer',
            author=self.user
        )
        views.Article.objects.create(
            title='пробная статья',
            slug='probnaya-statia',
            author=self.user
        )

        self.factory = RequestFactory()

class ArticleModelTestCase(Test_Vlog):

    def test_article_model_simple_load(self):
        instance = models.Article.objects.create()
        self.assertIsInstance(instance, models.Article)

    def test_article_model(self):
        article = models.Article.objects.get(title='Бег по утрам')
        self.assertEqual(article.slug, 'beg-po-utram')
        self.assertEqual(article.author, self.user)
        self.assertEqual(article.title, 'Бег по утрам')
        self.assertEqual(article.category.title, 'спорт')

    def test_article_name(self):
        article = models.Article.objects.get(title='Бег по утрам')
        expected_name = 'Бег по утрам'
        self.assertEqual(str(article), expected_name)


class CategoryModelTestCase(Test_Vlog):

    def test_category_model_simple_load(self):
        instance = models.Category.objects.create()
        self.assertIsInstance(instance, models.Category)

    def test_category_model(self):
        category = models.Category.objects.get(title='спорт')
        self.assertEqual(category.title, 'спорт')
        self.assertEqual(category.slug, 'sport')
        self.assertEqual(category.author, self.user)

    def test_category_name(self):
        category = models.Category.objects.get(title='спорт')
        expected_name = 'спорт'
        self.assertEqual(str(category), expected_name)


class CommentModelTestCase(Test_Vlog):

    def test_comment_model_simple_load(self):
        instance = models.Comment.objects.create()
        self.assertIsInstance(instance, models.Comment)

    def test_comment_model(self):
        comment = models.Comment.objects.get(author = self.user)
        self.assertEqual(comment.author, self.user)


class TagModelTestCase(Test_Vlog):

    def test_tag_model_simple_load(self):
        instance = models.Tag.objects.create()
        self.assertIsInstance(instance, models.Tag)

    def test_tag_model(self):
        tag = models.Tag.objects.get(title='бег')
        self.assertEqual(tag.title, 'бег')
        self.assertEqual(tag.slug, 'beh')

    def test_tag_name(self):
        tag = models.Tag.objects.get(title='бег')
        expected_name = 'бег'
        self.assertEqual(str(tag), expected_name)

class ArticleViewTestCase(Test_Vlog):

    def test_simple_load(self):
        instance = views.Article.objects.get(title='Бег по утрам')
        self.assertIsInstance(instance, views.Article)

    def article_test_view(self):
        article = views.Article.objects.get(title='пробная статья')

        self.assertEqual(article.title, 'пробная статья')
        self.assertEqual(article.slug, 'probnaya-statia')
        self.assertEqual(article.author, self.user)

class ArticlesViewTestCase(Test_Vlog):

    def test_articles(self):
        request = self.factory.get('/home/articles/')
        request.user = self.user
        response = views.ArticlesView.as_view()(request)
        self.assertEqual(response.status_code, 200)

class CategoriesViewTestCase(Test_Vlog):

    def test_articles(self):
        request = self.factory.get('/categories/')
        request.user = self.user
        response = views.CategoriesView.as_view()(request)
        self.assertEqual(response.status_code, 200)

class BaseViewTestCaseTestCase(Test_Vlog):

    def test_index(self):
        request = self.factory.get('/')
        request.user = self.user
        response = views.IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_base_view_template(self):
        self.assertEqual(BaseView.template_name, '')

    def test_base_view_simple_load(self):
        instance = BaseView()
        self.assertIsInstance(instance, BaseView)

    def test_home(self):
        request = self.factory.get('/home/')
        request.user = self.user
        response = views.IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)