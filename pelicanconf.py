#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#详细配置查看 http://docs.getpelican.com/en/3.4.0/settings.html

AUTHOR = u'liuwei'
SITENAME = u'Liuwei code'
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
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
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


DEFAULT_LANG = u'en'

TEMPLATE_PAGES = {
    "404.html": "404.html",
    "search.html": "search.html",
    "tags.html": "tags.html",
    "links.html": "links.html",
}

#################### 配置elegant主题
LANDING_PAGE_ABOUT={'title':'专注移动互联网，品味生活，做一个有思想的人！','details':'\
                                            <a href="http://weibo.com/u/3517080141?s=6uyXnP" target="_blank"><img border="0" src="http://service.t.sina.com.cn/widget/qmd/3517080141/93b4ea1e/1.png"/></a>\
                                            <br/><br/>大家好，我是刘伟，江苏<a href="http://baike.baidu.com/view/1136052.htm?from_id=14497&type=syn&fromtitle=宝应&fr=aladdin" target="_blank">宝应</a>人，爱好K歌，骑行。我是一个赶上80后末班车的屌丝男，一个被塑料压着鼻梁的眼镜男，一个成家还没有立业的已婚男。很显然，我还是一名IT男，因为热爱和坚持，我走到了今天，我相信，即使将来有一天IT不再是我挣钱的职业了，我也会继续走下去...\
                                            <br/><br/><img src="theme/icons/github.png"/>&nbsp;<a href="https://github.com/liuweicode" target="_blank">Github</a> \
                                            &nbsp;&nbsp;&nbsp;&nbsp;<img src="theme/icons/stackoverflow.png"/>&nbsp;<a href="https://stackoverflow.com/users/2968376/liu-wei" target="_blank">Stackoverflow</a> \
                                            &nbsp;&nbsp;&nbsp;&nbsp;<img src="theme/icons/twitter.png"/>&nbsp;<a href="https://twitter.com/liuweisays" target="_blank">Twitter</a> \
                                            &nbsp;&nbsp;&nbsp;&nbsp;<img src="theme/icons/facebook.png"/>&nbsp;<a href="https://www.facebook.com/profile.php?id=100008004043961" target="_blank">Facebook</a>'}
PROJECTS = [
                        {
                        'name': 'MonkeyRunner Tool',
                        'url': 'https://github.com/liuweicode/MonkeyRunnerTool',
                        'description': 'Android自动化测试，配置xml模拟一系列点击，拖动，长按等动作。'
                        },
                        {
                        'name': 'Weather Effects Demo',
                        'url': 'https://github.com/liuweicode/WeatherEffectsDemo',
                        'description': 'cocos2dx编写的天气效果，在ios和android平台上测试通过。'
                        },
                        {
                        'name': 'Base Project',
                        'url': 'https://github.com/liuweicode/BaseProject',
                        'description': '自定义类库，集成网络请求，错误日志邮件，以及一些自定义组件等，可以加速Android开发。'
                        },
                        {
                        'name': 'Page Curl Widget',
                        'url': 'https://github.com/liuweicode/PageCurlWidget',
                        'description': 'Android仿ios地图的半翻页效果组件'
                        },
                        {
                        'name': 'EXCEL TOOL',
                        'url': 'https://github.com/liuweicode/EXCELTOOL',
                        'description': '通过xml映射数据库表、数据表列，再通过poi将Excel中的数据导入到数据库中。'
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

#DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
