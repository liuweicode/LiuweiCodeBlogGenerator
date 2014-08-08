#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'liuwei'
SITENAME = u'Liuwei code'
SITEURL = 'http://liuwei.co'

PATH = 'content'
#模版主题 http://oncrashreboot.com/elegant-best-pelican-theme-features
THEME = "themes/pelican-elegant-1.3"
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

#################### 配置elegant主题
LANDING_PAGE_ABOUT={'title':'You can you up, no can no bibi','details':'You can write up your own About me section using LANDING_PAGE_ABOUT variable in your configuration. It is a dictionary that has two keys title and details. Value of title is displayed in the header of the home page, like in the above example it is “I design and build software products for iOS and OSX”. details is the text that appears under “About me” heading.'}
PROJECTS = [{
    'name': 'EXCEL TOOL',
    'url': 'https://github.com/liuweicode/EXCELTOOL',
    'description': 'Java通过poi将Excel数据导入到数据库'},
    {'name': 'PageCurlWidget',
    'url': 'https://github.com/liuweicode/PageCurlWidget',
    'description': 'Android仿ios半翻页效果组件'}]
    
PLUGIN_PATHS = ['plugins/sitemap']

PLUGINS=['sitemap',]

SITEMAP = {
        'format': 'xml',
        'priorities': {
                      'articles': 0.5,
                      'indexes': 0.5,
                      'pages': 0.5
                      },
        'changefreqs': {
                      'articles': 'monthly',
                      'indexes': 'daily',
                      'pages': 'monthly'
                      }
        }

####################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
DISQUS_SITENAME = 'suibian'
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

STATIC_PATHS = ['static']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
