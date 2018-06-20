{% extends 'core/base.tpl' %}

{% block title %}Tags{% endblock %}

{% block content %}
    <h3><a href="tags/">Теги:</a></h3>

    <ul>
    {% for article in articles %}
        <li>
            <a href="/categories/{{ article.category__slug }}/articles/{{ article.slug }}">
                {{ article.title }} </a> [ {{ article.category__title }} ]
        </li>
    {% endfor %}
    </ul>
{% endblock %}