<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>woshiceshi</title>
</head>
<body>
TEST

<s:iterator value="userList" id="ulist">
	<tr>
		<td><s:property value="#ulist.userName"/></td>
		<td><s:property value="#ulist.telephone"/></td>
	</tr>
</s:iterator>


<%-- <a type="button" href="users/test">测试action</a>

<s:form action name="findAllUser" namespace="/users" executeResult="true">
<s:param name="userList" value="userList"></s:param> 
<s:param name="telephone" value="telephone"></s:param> 
</s:form>

<s:iterator value="userList" id="ulist">
	<s:property />
</s:iterator>

<s:iterator value="{'1','2','3','4','5'}" id='number'>
    <s:property value='number'/>A
</s:iterator> --%>
</body>
</html>