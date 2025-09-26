---
layout: page
title: "fullcommit"
---

Welcome to fullcommit — a living notebook of Python studies, projects, and pro tips.

## Recent Posts

{% assign posts = site.posts %}
{% if posts.size == 0 %}
<p>No posts yet. Check back soon!</p>
{% else %}
<div>
  {% for post in posts %}
  <article>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p><small>{{ post.date | date: "%b %-d, %Y" }}</small></p>
    {% if post.excerpt %}
      <p>{{ post.excerpt | strip_html | truncate: 200 }}</p>
    {% endif %}
    <p><a href="{{ post.url | relative_url }}">Read more →</a></p>
    <hr />
  </article>
  {% endfor %}
</div>
{% endif %}

<p>
  <a href="{{ "/debug/" | relative_url }}">Debug</a> ·
  <a href="{{ "/about/" | relative_url }}">About</a>
  
</p>


