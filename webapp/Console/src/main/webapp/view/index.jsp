<%@ page language="java" contentType="text/html; charset=utf-8"
	pageEncoding="utf-8"%>
<%@ taglib prefix="s" uri="/struts-tags"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
<base href="<%=request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + request.getContextPath()%>/" />
<link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Monitor</title>
	<%--<style >
		img{
			margin:100px auto 0;
			-moz-transform:rotate(90deg);
			-webkit-transform:rotate(90deg);
			filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=3);

		}
	</style>--%>
</head>

<body>
	<div style="width:800px; margin:0 auto;" >
	
	<input type="text" id="search" onkeyup="searchUsers(this.value)"
		placeholder="查询联系人" class="form-control" style="margin-top: 30px">
	<button data-toggle="modal" data-size="modal-lg"
			data-target="#addUser"  class="btn btn-primary" style="float:right;margin-bottom: 10px;margin-top: 10px">添加</button>
	<table id="informationTable" class="table table-striped table-bordered table-hover"></table>
	
	</div>
							
	<div class="modal fade" id="addUser">
		<div class="modal-dialog">
			<div class="modal-content">

				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal"
						aria-hidden="true">×</button>
					<h4 class="modal-title">添加人员</h4>
				</div>
				<div class="modal-body">
					<div class="form-horizontal">

						<div class="form-group">
							<label class="col-sm-2 control-label">姓名</label>
							<div class="col-sm-10">
								<input type="text" class="form-control front-no-box-shadow"
									id="userName">
							</div>
						</div>

						<div class="form-group">
							<label class="col-sm-2 control-label">电话</label>
							<div class="col-sm-10">
								<input type="text" class="form-control front-no-box-shadow"
									id="userTelephone">
							</div>
						</div>

					</div>
				</div>
				<div class="modal-footer">
					<button class="btn btn-default" data-dismiss="modal">取消</button>
					<button class="btn btn-primary" onclick="addUsers()">完成</button>
				</div>

			</div>
		</div>
	</div>

	<%--<div>
		<img id="viewImg2" src="img/fandog.jpg"  style="height:200px;width:400px;text-align: center;" >
	</div>--%>

	<script src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.js"></script>
	<script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
	<script src="js/index.js" charset="utf-8"></script>
</body>
</html>