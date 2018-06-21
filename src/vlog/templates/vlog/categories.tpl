{% extends 'core/base.tpl' %}

{% block title %}Categories{% endblock %}
{% block breadcrumbs %}
    {{ super ()}}<a href="categories/">Категории</a>
{% endblock %}

{% block content %}
    <h3><a href="categories/">Категории:</a></h3>


    <ul>
    {% for category in categories %}
        <li>
            <a href="categories/{{ category.slug }}">{{ category.title }}</a>
        </li>

    {% endfor %}
    </ul>
{% endblock %}