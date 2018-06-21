<nav class="navbar navbar-dark bg-primary">
    <span class="navbar-text">
        <a class="navbar-brand" href="{{ url('vlog:index') }}">{{ _('Blog') }}</a>
    </span>
    {% if user.is_authenticated %}
        <span class="navbar-text">
            {{ _('Hello') }}, {{ user.username }}!&nbsp;<a href="{{ url('logout') }}">{{ _('GTFO!') }}</a>
        </span>
    {% endif %}
</nav>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="/home">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/categories">Categories</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/tags">Tags</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Login/Logout</a>
      </li>
      <li class="nav-item">
      </li>

      </ul>

  </div>
</nav>