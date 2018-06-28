{% extends 'core/base.tpl' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h3>Home</h3>

    <hr>

    <h3><a href="categories/">Популярные категории:</a></h3>

    <ul>
    {% for category in categories %}
        <li>
            <a href="categories/{{ category.slug }}/">{{ category.title }}</a>
        </li>
    {% endfor %}
    </ul>

    <br>

    <h3><a href="articles/">Популярные статьи:</a></h3>
    <ul>
    {% for article in articles %}
        <li>
            <a href="/categories/{{article.category.slug}}/articles/{{ article.slug }}/">{{ article.title }}</a>
        </li>
    {% endfor %}
    </ul>

    <br>

    <h3><a href="tags/">Лучшие теги</a></h3>
    <ul>
    {% for tag in tags %}
        <li>
            <a href="tags/{{ tag.slug }}/">{{ tag.title }}
        </li>
    {% endfor %}
    </ul>
{% endblock %}