
{% extends "core/base.tpl" %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ tag.title }}{% endblock %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, tag.title) }}
{% endblock %}

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