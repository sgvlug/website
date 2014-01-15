#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SGVLUG'
SITENAME = u'SGVLUG'
SITESUBTITLE = u"San Gabriel Valley Linux User's Group"
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ( ('Mailing List', 'http://sgvlug.net/mailman/listinfo/sgvlug'),
          ('Meetup Group', 'http://www.meetup.com/SGVTech/'),
          ('SGVHAK', 'http://www.sgvhak.org/'), 
          ('IRC: #sgvlug on Freenode', 'http://webchat.freenode.net/?channels=sgvlug') )

# Social widget
SOCIAL =  None

DEFAULT_PAGINATION = 6 
SUMMARY_MAX_LENGTH = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

STATIC_PATHS = ['images', 'slides', "favicon.png", "CNAME"]

THEME = 'theme/bootstrap3'
BOOTSTRAP_THEME = 'cosmo'

PAGES_NAME = 'Info'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_PAGES_ON_SIDEBAR = True
DISPLAY_LINKS_ON_SIDEBAR = True

SHOW_EVENT_INFO = True
DEFAULT_DATE_FORMAT = '%A %B %d, %Y %I:%M %p'

from pelican.utils import get_date, strftime
def format_date(value, date_format=DEFAULT_DATE_FORMAT):
    return strftime(get_date(value), date_format)

JINJA_FILTERS = { 'format_date': format_date, }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
