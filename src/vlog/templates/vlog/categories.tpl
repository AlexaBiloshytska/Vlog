{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, 'Categories') }}
{% endblock %}

{% block content %}
    <h3><a href="categories/">Категории:</a></h3>
    <ul>
    {% for category in categories %}
        <li>
            <a href="/categories/{{ category.slug }}">{{ category.title }}</a>
        </li>
    {% endfor %}


    <div class="pagination">
        <span class="step-links">
            {% if categories.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ categories.previous_page_number }}&q={{ request.GET.q1 }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ categories.number }} of {{ categories.paginator.num_pages }}.
            </span>

            {% if categories.has_next %}
                <a href="?page={{ categories.next_page_number }}&q1={{ request.GET.q1 }}">next</a>
                <a href="?page={{ categories.paginator.num_pages }}&q1={{ request.GET.q1 }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>
{% endblock %}