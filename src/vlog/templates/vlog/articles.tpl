 {% extends 'core/base.tpl' %}

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

    <div class="pagination">
    <span class="step-links">
        {% if articles.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ articles.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ articles.number }} of {{ articles.paginator.num_pages }}.
        </span>

        {% if articles.has_next %}
            <a href="?page={{ articles.next_page_number }}">next</a>
            <a href="?page={{ articles.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>

{% endblock %}