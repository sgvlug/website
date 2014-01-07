#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SGVLUG'
SITENAME = u"SGVLUG - San Gabriel Valley Linux User's Group"
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ( ('Mailing List', 'http://sgvlug.net/mailman/listinfo/sgvlug'),
          ('SGVHAK', 'http://www.sgvhak.org/'), )

# Social widget
SOCIAL =  None

DEFAULT_PAGINATION = 10 
SUMMARY_MAX_LENGTH = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

STATIC_PATHS = ['images', 'slides']

THEME = 'theme/bootstrap3'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_PAGES_ON_SIDEBAR = True
DISPLAY_LINKS_ON_SIDEBAR = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
