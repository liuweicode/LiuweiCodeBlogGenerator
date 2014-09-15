Title: HttpSessionBinding接口
Date: 2009-10-03 11:55
Category: Java
Tags: java
Authors: Liuwei

如果一个对象实现了HttpSessionBindingListener 接口，当这个对象被绑定到Session 中或者从Session 中
被删除的时候，Servlet容器会通知这个对象，而这个对象在接收到通知后，可以做一些初始化或者清除状态
的操作。

方法介绍 ：

javax.servlet.http.HttpSessionBindingListener 接口提供了下面的方法：

1、 public void valueBound(HttpSessionBindingEvent event)
当对象正在被绑定到Session 中，Servlet 容器调用该方法来通知该对象。

2、 public void valueUnbound(HttpSessionBindingEvent event)
当从Session 中删除对象时，Servlet 容器调用该方法来通知该对象。
Servlet 容器通过 HttpSessionBindingEvent 对象来通知实现了 HttpSessionBindingListener 接口的对象，而这个
对象可以利用HttpSessionBindingEvent 对象来访问与它相联系的HttpSession 对象.

javax.servlet.http.HttpSessionBindingEvent 类提供了一下两种方法：

public HttpSessionBindingEvent(HttpSession session, java.lang.String name)

public HttpSessionBindingEvent(HttpSession session, java.lang.String name,java.lang.Object value)

上面两个构造方法构造一个事件对象，当一个对象被绑定到Session 中或者从Session 中被删除的时候，用这
个事件对象来通知它。

public java.lang.String getName()
返回绑定到Session 中或者从Session 中被删除的属性的名字。

public java.lang.Object getValue()
返回被添加。删除或替换的属性的值，如果属性被添加或者被删除，这个方法返回属性的值，如果属性被替
换，这个方法返回属性先前的值。

public HttpSession getSession()
返回HttpSession 对象。

案例：在线人数统计程序

index.jsp

	<%@ page language=”java” import=”java.util.*” pageEncoding=”GBK”%>
	<%
	String path = request.getContextPath();
	String basePath =
	request.getScheme()+”://”+request.getServerName()+”:”+request.getServerPort()+
	path+”/”;
	%>
	<!DOCTYPE HTML PUBLIC “-//W3C//DTD HTML 4.01 Transitional//EN”>
	<html>
	<head>
	<base href=”<%=basePath%>”>
	<title>My JSP ‘index.jsp’ starting page</title>
	<meta http-equiv=”pragma” content=”no-cache”>
	<meta http-equiv=”cache-control” content=”no-cache”>
	<meta http-equiv=”expires” content=”0″>
	<meta http-equiv=”keywords” content=”keyword1,keyword2,keyword3″>
	<meta http-equiv=”description” content=”This is my page”>
	<!–
	<link rel=”stylesheet” type=”text/css” href=”styles.css” mce_href=”styles.css”>
	–>
	</head>
	<body>
	<form action=”CheckLogin” method=”post”>
	<table>
	<tr><td>用户名：</td><td><input type=”text” name=”name”/></td></tr>
	<tr><td>密码：</td><td><input type=”password” name=”pass”/></td></tr>
	<tr><td colspan=”2″ align=”right”><input type=”reset” value=” 清 空
	“/> <input type=”submit” value=”登陆”/></td></tr>
	</table>
	</form>
	</body>
	</html>


CheckLogin.java

	packagepackagepackagepackage com.accp.demo.servlet;
	importimportimportimport java.io.IOException;
	importimportimportimport javax.servlet.ServletException;
	importimportimportimport javax.servlet.http.HttpServlet;
	importimportimportimport javax.servlet.http.HttpServletRequest;
	importimportimportimport javax.servlet.http.HttpServletResponse;
	importimportimportimport javax.servlet.http.HttpSession;
	importimportimportimport com.accp.demo.chatonline.User;
	publicpublicpublicpublic classclassclassclass CheckLogin extendsextendsextendsextends HttpServlet {
	publicpublicpublicpublic voidvoidvoidvoid doGet(HttpServletRequest request, HttpServletResponse response)
	throwsthrowsthrowsthrows ServletException, IOException {
	doPost(request,response);
	}
	publicpublicpublicpublic voidvoidvoidvoid doPost(HttpServletRequest request, HttpServletResponse response)
	throwsthrowsthrowsthrows ServletException, IOException {
	request.setCharacterEncoding(“GBK”);
	String name = request.getParameter(“name”);
	String pass = request.getParameter(“pass”);
	ifififif (nullnullnullnull == name || pass==nullnullnullnull) {
	request.getRequestDispatcher(“index.jsp”)
	.forward(request, response);
	returnreturnreturnreturn;
	}
	HttpSession session=request.getSession();
	session.setAttribute(“user”, newnewnewnew User(name));
	response.sendRedirect(“userlist.jsp”);
	}
	}


User.java

	packagepackagepackagepackage com.accp.demo.chatonline;
	importimportimportimport javax.servlet.http.HttpSessionBindingEvent;
	importimportimportimport javax.servlet.http.HttpSessionBindingListener;
	publicpublicpublicpublic classclassclassclass User implementsimplementsimplementsimplements HttpSessionBindingListener {
	privateprivateprivateprivate String name;
	privateprivateprivateprivate UserList userList = UserList.getInstance();
	publicpublicpublicpublic User() {
	}
	publicpublicpublicpublic User(String name) {
	thisthisthisthis.name = name;
	}
	publicpublicpublicpublic String getName() {
	returnreturnreturnreturn name;
	}
	publicpublicpublicpublic voidvoidvoidvoid setName(String name) {
	thisthisthisthis.name = name;
	}
	publicpublicpublicpublic voidvoidvoidvoid valueBound(HttpSessionBindingEvent arg0) {
	userList.addUser(name);
	}
	publicpublicpublicpublic voidvoidvoidvoid valueUnbound(HttpSessionBindingEvent arg0) {
	userList.removeUser(name);
	}
	}


UserList.java

	packagepackagepackagepackage com.accp.demo.chatonline;
	importimportimportimport java.util.Enumeration;
	importimportimportimport java.util.Vector;
	/**
	* 单例类
	* 统计在线人数
	*@author@author@author@author 刘伟
	*
	*/
	publicpublicpublicpublic classclassclassclass UserList {
	privateprivateprivateprivate staticstaticstaticstatic finalfinalfinalfinal UserList userList=newnewnewnew UserList();
	privateprivateprivateprivate Vector<String> v;
	//私有的构造方法
	privateprivateprivateprivate UserList(){
	v=newnewnewnew Vector<String>();
	}
	//获得实例
	publicpublicpublicpublic staticstaticstaticstatic UserList getInstance(){
	returnreturnreturnreturn userList;
	}
	publicpublicpublicpublic voidvoidvoidvoid addUser(String name){
	ifififif(nullnullnullnull!=name){
	v.add(name);
	}
	}
	publicpublicpublicpublic voidvoidvoidvoid removeUser(String name){
	ifififif(nullnullnullnull!=name){
	v.remove(name);
	}
	}
	publicpublicpublicpublic Enumeration<String> getUserList(){
	returnreturnreturnreturn v.elements();
	}
	publicpublicpublicpublic intintintint getUserCount(){
	returnreturnreturnreturn v.size();
	}
	}


Userlist.jsp

	<%@ page language=”java” import=”java.util.*” pageEncoding=”GBK”%>
	<%@page import=”com.accp.demo.chatonline.UserList”%>
	<%
	String path = request.getContextPath();
	String basePath =
	request.getScheme()+”://”+request.getServerName()+”:”+request.getServerPort()+
	path+”/”;
	%>
	<!DOCTYPE HTML PUBLIC “-//W3C//DTD HTML 4.01 Transitional//EN”>
	<html>
	<head>
	<base href=”<%=basePath%>”>
	<title>My JSP ‘userlist.jsp’ starting page</title>
	<meta http-equiv=”pragma” content=”no-cache”>
	<meta http-equiv=”cache-control” content=”no-cache”>
	<meta http-equiv=”expires” content=”0″>
	<meta http-equiv=”keywords” content=”keyword1,keyword2,keyword3″>
	<meta http-equiv=”description” content=”This is my page”>
	<!–
	<link rel=”stylesheet” type=”text/css” href=”styles.css” mce_href=”styles.css”>
	–>
	</head>
	<body>
	<%
	UserList ul=UserList.getInstance();
	Enumeration<String> e=ul.getUserList();
	out.print(“当前在线用户：<br>”);
	whilewhilewhilewhile(e.hasMoreElements()){
	out.print(e.nextElement()+”<br>”);
	}
	%>
	<a href=”servlet/LoginOut” mce_href=”servlet/LoginOut”>注销</a>
	</body>
	</html>


LoginOut.java

	packagepackagepackagepackage com.accp.demo.servlet;
	importimportimportimport java.io.IOException;
	importimportimportimport java.io.PrintWriter;
	importimportimportimport javax.servlet.ServletException;
	importimportimportimport javax.servlet.http.HttpServlet;
	importimportimportimport javax.servlet.http.HttpServletRequest;
	importimportimportimport javax.servlet.http.HttpServletResponse;
	importimportimportimport javax.servlet.http.HttpSession;
	importimportimportimport com.accp.demo.chatonline.User;
	publicpublicpublicpublic classclassclassclass LoginOut extendsextendsextendsextends HttpServlet {
	publicpublicpublicpublic voidvoidvoidvoid doGet(HttpServletRequest request, HttpServletResponse response)
	throwsthrowsthrowsthrows ServletException, IOException {
	HttpSession session=request.getSession();
	String name=((User)session.getAttribute(“user”)).getName();
	session.invalidate();
	response.setContentType(“text/html;charset=GBK”);
	response.getWriter().print(“<mce:script
	language=’javascript’><!–
	alert(‘”+name+” 用 户 已 退 出
	‘);location.replace(‘../index.jsp’);
	// –></mce:script>”);
	}
	publicpublicpublicpublic voidvoidvoidvoid doPost(HttpServletRequest request, HttpServletResponse response)
	throwsthrowsthrowsthrows ServletException, IOException {
	doGet(request,response);
	}
	}


web.xml

	<?xml version=”1.0″ encoding=”UTF-8″?>
	<web-app version=”2.5″
	xmlns=”http://java.sun.com/xml/ns/javaee”
	xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance”
	xsi:schemaLocation=”http://java.sun.com/xml/ns/javaee
	http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd”>
	<servlet>
	<servlet-name>CheckLogin</servlet-name>
	<servlet-class>com.accp.demo.servlet.CheckLogin</servlet-class>
	</servlet>
	<servlet>
	<servlet-name>LoginOut</servlet-name>
	<servlet-class>com.accp.demo.servlet.LoginOut</servlet-class>
	</servlet>
	<servlet-mapping>
	<servlet-name>CheckLogin</servlet-name>
	<url-pattern>/CheckLogin</url-pattern>
	</servlet-mapping>
	<servlet-mapping>
	<servlet-name>LoginOut</servlet-name>
	<url-pattern>/servlet/LoginOut</url-pattern>
	</servlet-mapping>
	<welcome-file-list>
	<welcome-file>index.jsp</welcome-file>
	</welcome-file-list>
	</web-app>

