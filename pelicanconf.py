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
LANDING_PAGE_ABOUT={'title':'You can you up, no can no bibi','details':'专注IT，品味生活，做一个有思想的人！<br/>大家好，我是刘伟，一个赶上80后末班车的屌丝男，一个被镜片压着鼻梁的眼镜男，一个成家还没有立业的已婚男。很显然，我是一名程序员，闲暇之余喜欢K歌，骑车等。'}
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
