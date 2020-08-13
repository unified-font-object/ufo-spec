---
layout: default
navigation: true
order: 5
title: Contributors
---

The UFO format was created by Just van Rossum, Erik van Blokland and Tal Leming. The specification is managed and maintained by:

- Tal Leming
- Erik van Blokland
- Just van Rossum
- Ben Kiel
- Frederik Berlaen

The UFO specification is a community project with input and edits from many people, including:

{% for contributor in site.github.contributors %}
	{% if contributor.contributions > 1 %}
		{% assign c = "edits" %}
	{% else %}
		{% assign c = "edit" %}
	{% endif %}
- [{{ contributor.login }}]({{ contributor.html_url }}) – {{ contributor.contributions }} {{ c }}
{% endfor %}

## Site Credits

The typefaces used on this site are from the [IBM Plex](https://www.ibm.com/plex/) family designed by [Bold Monday](https://www.boldmonday.com) and a wide array of collaborators.