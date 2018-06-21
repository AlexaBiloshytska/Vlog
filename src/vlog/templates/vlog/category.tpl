 {% extends 'core/base.tpl' %}

{% block title %}Category{% endblock %}
{% block breadcrumbs %}
    {{ super() }}
{% endblock %}

{% block content %}
    <h3>Категория: {{ category.title }}</h3>


    <h4>Most commented articles in category:</h4>
    <ul>
    {% for article in articles %}
        <li>
            <a href="articles/{{ article.slug }}/">{{ article.title }}</a>
            <p> {{ article.description }} </p>
        </li>
    {% endfor %}
    </ul>

    <h4>All articles in category:</h4>
    <ul>
    {% for article in articlesAll %}
        <li>
            <a href="articles/{{ article.slug }}/">{{ article.title }}</a>
        </li>
    {% endfor %}
    </ul>

{% endblock %}