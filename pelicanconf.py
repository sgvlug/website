#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SGVLUG'
SITENAME = u'SGVLUG'
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = None

# Social widget
SOCIAL =  None

DEFAULT_PAGINATION = 10 
SUMMARY_MAX_LENGTH = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

STATIC_PATHS = ['images', 'slides']

THEME = 'theme/bootstrap3'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
