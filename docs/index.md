---
layout: page
title: "fullcommit"
---

Welcome to fullcommit — a living notebook of Python studies, projects, and pro tips.

## Recent Posts

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span> — {{ post.date | date: "%b %-d, %Y" }}</span>
  </li>
{% endfor %}
<ul>


