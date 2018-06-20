{% extends 'core/base.tpl' %}

{% block title %}Article{% endblock %}

{% block content %}
    <h3> Article: {{ article.title }}</h3>

    {% if article.image %}
        <img src = "{{article.image}}">
    {% endif %}

    {% autoescape off %} {{ article.content }} {% endautoescape %}

{% endblock %}