
{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{% endblock %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, article.title) }}
{% endblock %}

{% block content %}
    <h1 class="blog-post-title">{{ article.title }}</h1>
    <div class="blog-post">
        <p>{{ article.content|safe }}</p>
    </div>
    <ul>
    {% for article in articles %}
        <li>
            <a href="{{ article.slug }}">{{ article.title }}</a>
        </li>
    {% endfor %}
    </ul>
{% endblock %}