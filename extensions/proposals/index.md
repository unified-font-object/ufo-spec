---
layout: default
navigation: true
order: 1100
title: Proposals
---

Active proposals to extend or improve the Designspace or UFO specifications are listed on this page while they are maturing. Once accepted into the official specification, they will be moved to the appropriate section.

{% for proposal in site.proposals %}
<h2><a href="{{ proposal.url }}">{{ proposal.title }}</a></h2>

{{ proposal.summary_md | markdownify }}

<p><a href="{{ proposal.url }}">Full proposal →</a></p>
{% endfor %}
