{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, 'Articles') }}
{% endblock %}

{% block title %}Articles{% endblock %}


{% block content %}
    <h3>Most commented articles in category: {{ category.title }}</h3>

    <ul>
    {% for article in articles %}
        <li>
            <a href="{{ article.slug }}">{{ article.title }}</a>
        </li>
    {% endfor %}
    </ul>

{% endblock %}