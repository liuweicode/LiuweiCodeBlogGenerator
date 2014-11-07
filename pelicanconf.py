#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#详细配置查看 http://docs.getpelican.com/en/3.4.0/settings.html

AUTHOR = u'liuwei'
SITENAME = u'刘伟博客'
#SITEURL = 'http://localhost:8000'
SITEURL = 'http://liuwei.co'

PATH = 'content'
#模版主题 http://oncrashreboot.com/elegant-best-pelican-theme-features
THEME = "themes/pelican-elegant-1.3"
TIMEZONE = 'Asia/Shanghai'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#使用文件名作为文章或页面的slug（url）
FILENAME_METADATA = '(?P<slug>.*)'
#页面的显示路径和保存路径，推荐下面的方式
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'

RECENT_ARTICLES_COUNT = 20

DEFAULT_LANG = u'en'

TEMPLATE_PAGES = {
    "404.html": "404.html",
    "search.html": "search.html",
    "tags.html": "tags.html",
    "links.html": "links.html",
}


#################### 配置elegant主题
LANDING_PAGE_ABOUT={'title':'品味老歌 感动生活 记录每个值得记忆的瞬间！','details':'\
                                           大家好，我是刘伟，江苏<a href="http://baike.baidu.com/view/1136052.htm?from_id=14497&type=syn&fromtitle=宝应&fr=aladdin" target="_blank">宝应</a>人，爱好K歌，骑行。我是一个赶上80后末班车的屌丝男，一个被塑料压着鼻梁的眼镜男，一个成家还没有立业的已婚男。'
                                           }



PROJECTS = [
                        {
                        'name': '结婚一周年纪念日',
                        'url': 'http://v.youku.com/v_show/id_XNjE2MDExNzA4.html',
                        'description': 'http://v.youku.com/v_show/id_XNjE2MDExNzA4.html'
                        },
                        {
                        'name': '结婚两周年纪念日',
                        'url': 'http://v.youku.com/v_show/id_XNzk0NDQ1ODI0.html',
                        'description': 'http://v.youku.com/v_show/id_XNzk0NDQ1ODI0.html'
                        }
                    ]

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

# 链接
LINKS = (
                 ('Pelican', 'http://getpelican.com/'),
                 ('Python.org', 'http://python.org/'),
                 ('Jinja2', 'http://jinja.pocoo.org/'),
              )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

STATIC_PATHS = ['static']
#EXTRA_PATH_METADATA = {
#    'static/*': {'path': 'posts/static/*'},
#}

#DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
