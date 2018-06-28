{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, 'Tags') }}
{% endblock %}

{% block content %}
    <h2>Теги:</h2>

    {% for tag in tags %}

        <h3><a href="/tags/{{ tag.slug }}/">{{ tag.title }}</a></h3>

        {% set count = [3] %}

        <ul>
        {% for article in articles if article.tags == tag.id and count[0] > 0 %}
            <li><a href="/article/{{ article.slug }}/">{{ article.title }}</a></li>
            {% if count.append(count.pop() - 1) %} {% endif %}
        {% endfor %}
        </ul>
    {% endfor %}
    <br>
{% endblock %}

