LiuweiCodeBlogGenerator
=======================

使用 pelican 生成静态博客：http://liuwei.co

#### clone 仓库

	git clone https://github.com/liuweicode/LiuweiCodeBlogGenerator.git
	
#### 在content目录下写文章

	Title: Linux 下制作Gif动画 
	Date: 2013-02-01 10:11
	Modified: 2013-02-01 10:11
	Category: Linux
	Tags: ubuntu, ffmpeg, gif
	Slug: make-gif-on-linux
	Authors: liuwei
	Summary: 简介简介简介简介
	
	内容内容内容内容内容内容内容内容内容内容
	
#### 生成静态网站 本地查看

	make clean
	make html
	make publish
	make serve
	
打开浏览器 http://localhost:8000
	
#### 提交到github liuweicode.github.io

	git add --all
	git commit -m "提交内容"
	git push origin master

