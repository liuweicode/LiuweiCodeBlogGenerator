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

TEMPLATE_PAGES = {
    "404.html": "404.html",
    "search.html": "search.html",
}

#################### 配置elegant主题
LANDING_PAGE_ABOUT={'title':'You can you up, no can no bibi','details':'专注IT，品味生活，做一个有思想的人！<br/>大家好，我是刘伟，江苏扬州人士，爱好K歌，骑车，我是一个赶上80后末班车的屌丝男，一个被塑料压着鼻梁的眼镜男，一个成家还没有立业的已婚男。很显然，我是一名IT男，08年入行，09年夏末进入上海REACH进出口有限公司实习，做公司内部网站，后因该公司并不是纯粹的软件开发公司，遂在09年年底递上辞职信一封，离开了REACH，后因无学历，无工作经验在家待业，陷入了人生的低谷，无奈之下，进入上海宝山区大华路乐购超市学起了烘培技术，期间学会了做各式面包，披萨等，但也将IT技术荒废了一年之久，几乎忘的一干二净！11年在老家过完春节回到上海，3月15日，这一天是我人生的转折点，我在招聘网站拨打了上海巍运信息科技有限公司的电话，并主动要求上门面试，在当天下午便通过了面试，第二天以20RMB/天的薪资来公司实习，过了三天左右取消了实习转为试用，又过了大半个月之后，取消试用期两个月的约定，直接转为正式员工了，后面一切都比较顺利，薪水也涨的比较满意（当然是比不上通货膨胀和房价的）。在13年年底，由于另一家公司开出了高很多的薪水，我便提出了辞职，但因各种错中复杂的原因，我没有选择去那家公司，今年两月底，我入职了上海楼顶网络科技有限公司，我目前的职业生涯就是这样，因为热爱和坚持，我走到了今天，即使将来有一天IT不再是我的挣钱的职业了，我相信我也会继续走下去...'}
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
