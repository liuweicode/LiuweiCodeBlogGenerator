Title: Ubuntu 通过ipv4转ipv6上网 
Date: 2012-12-04 05:45
Modified: 2012-12-04 05:45
Category: Ubuntu
Tags: ubuntu, ipv6, ipv4
Slug: connect-with-ipv6-on-ubuntu
Authors: liuwei
Summary: Ubuntu 通过ipv4转ipv6上网

	sudo apt-get install miredo
	sudo gedit /etc/hosts

将如下网址的内容粘贴进去：<https://ipv6-hosts.googlecode.com/hg/hosts>

	sudo gedit /etc/default/ufw
	
修改：IPV6=yes
重启防火墙

	sudo ufw disable
	sudo ufw enable

参考：<https://wiki.ubuntu.com/IPv6#Get_connected_with_Miredo>
