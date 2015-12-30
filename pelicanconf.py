#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'uelei'
SITENAME = u'blog uelei.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HEADER_COVER = 'static/images/img_3661.jpg'

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('You can modify those links in your config file', '#'),)

DELETE_OUTPUT_DIRECTORY = True

TWITTER_USERNAME = "uelei"
GITHUB_URL = "https://github.com/uelei"
# DISQUS_SITENAME = "mathieuleplatre"
# PIWIK_URL = "mathieu-leplatre.info/piwik"
# PIWIK_SITE_ID = 1
TWITTER_URL = 'http://twitter.com/uelei'
FACEBOOK_URL = 'http://facebook.com/uelei'

COLOR_SCHEME_CSS = 'monokai.css'

SOCIAL = (
    # ("LinkedIn", "http://www.linkedin.com/in/leplatre"),
    # ("Launchpad", "https://code.launchpad.net/~mathieu.leplatre"),
    ("GitHub", "https://github.com/uelei"),
    # ("Google+", "https://plus.google.com/u/0/106965745149150173373"),
    ("Twitter", "http://twitter.com/uelei"),
    # ("Identi.ca", "http://identi.ca/leplatrem"),
)
DEFAULT_PAGINATION = 10

PLUGINS = [
    'pelican_gist',
]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['static', 'static/extra/CNAME', 'static/extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'static/extra/CNAME': {'path': 'CNAME'},
    'static/extra/favicon.ico': {'path': 'favicon.ico'},
}
