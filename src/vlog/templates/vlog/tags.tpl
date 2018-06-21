{% extends 'core/base.tpl' %}

{% block title %}Tags{% endblock %}
{% block breadcrumbs %}
    {{ super() }}<a href="/tags">Tags</a>
{% endblock %}
{% block content %}
    <h2>Теги:</h2>

    {% for tag in tags %}

        <h3><a href="/tags/{{ tag.slug }}/">{{ tag.title }}</a></h3>

        {% set count = [3] %}

        <ul>
        {% for article in articles if article.tags == tag.id and count[0] > 0 %}
            <li><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></li>
            {% if count.append(count.pop() - 1) %} {% endif %}
        {% endfor %}
        </ul>
    {% endfor %}
    <br>
{% endblock %}