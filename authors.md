---
layout: page
title: Authors
description: A listing of all the authors.
nav_exclude: false
---

# Authors
{% for author in site.authors %}
{{ author }}
{% endfor %}
