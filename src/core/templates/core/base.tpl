<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap.min.css">
        <link rel="stylesheet" href="{{ STATIC_URL }}css/blog.css">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block navbar %}
            {% include 'core/navbar.tpl' %}
         {% endblock %}

         <ol class="breadcrumb my-4">
            {% block breadcrumb %}
            {% endblock %}
           </ol>

        <br>

        <div class="container-fluid">
            {% block content %}
            {% endblock %}
        </div>

        {% block footer %}
            {% include 'core/footer.tpl' %}
        {% endblock %}
    </body>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
</html>