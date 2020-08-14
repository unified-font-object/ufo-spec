---
layout: default
navigation: true
order: 1000
title: Lib and data
---

The Designspace and UFO formats allow arbitrary information to be associated with various objects of the format.
These pages aim to provide informal specification for all lib keys and data files that may be used by more than one authoring tool or compiler.

This documentation effort only concerns versions 4+ of Designspace and 3+ of UFO.

{% for lib_and_data in site.lib_and_data %}
<h2><a href="{{ lib_and_data.url }}">{{ lib_and_data.title }}</a></h2>

<p>{{ lib_and_data.summary }}</p>

<ul>
{% for key in lib_and_data.lib_and_data_keys %}
    <li>
    <a href="{{ lib_and_data.url }}#{{ key.location | slugify }}_{{ key.name | slugify }}">
        <code>{{ key.name }}</code>
    </a>
    </li>
{% endfor %}
</ul>
{% endfor %}
