---
layout: page
title: Welcome
tagline: 
---
{% include JB/setup %}

### Upcoming / Most Recent Meeting

<div>
{% assign found_first_meeting = false %}
{% for post in site.posts %}
  {% if post.category == "meetings" and found_first_meeting == false %}
    {% assign found_first_meeting = true %}
    <div><span>{% if post.meetingdate %}{{ post.meetingdate | date_to_long_string }}{% else %}{{ post.date | date_to_string }}{% endif %}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a> {{ post.content | markdownify  }}</div>
  {% endif %}
{% endfor %}
</div>

### About

SGVLUG attracts members from throughout the Los Angeles basin, Pasadena, Glendale, Burbank, and eastward along the San Gabriel Mountains.

General Meeting: Our primary meeting is held on the 2nd Thursday of every month
Time: 7-9pm 
Location: Downs building, room 107, on the Caltech Campus in Pasadena (while the campus address is technically 1200 california street, the campus is quite large. The Downs building is across from the tennis courts on California at Arden)

Maps: <a href="http://www.caltech.edu/map/main.html?bn=47">Campus Map</a> -- <a href="{{ BASE_PATH}}/pages/map.html">Area Map</a>

### Useful Information

<ul>
{% assign pages_list = site.pages %}
{% assign group = "info" %}
{% include JB/pages_list %}
</ul>

### Mailing List

You can join by going to the <a href="http://sgvlug.org/mailman/listinfo/sgvlug">SGVLUG e-mail sign-up page</a>

We maintain an archive of all messages posted to the list. If you are concerned about the possibility that your e-mail address might become "harvested" because it is on a web page, see this item in the FAQs about <a href="{{ BASE_PATH }}pages/email_no_archive.html">"how to avoid having your e-mail archived"</a>