$.ajaxSetup({ 
    scriptCharset: "utf-8",
    contentType: "application/json; charset=utf-8"
});

$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "users/findAllUser",
        dataType : 'json',
		success : function(data) {
			$("#informationTable").html('');
			$("#informationTable").html('<TR><TD>姓名</TD><TD>电话</TD></TR>');
			$(data.userList).each(function(i, value) {
				$("#informationTable").append('<TR><TD>'+ value.userName
								+'</TD><TD>'+value.telephone+'</TD><TD>'+
								'<input type="button" style="float:right" value="删除" class="btn btn-primary"'+
								' onclick="deleteUsers('+value.id+',this)"></TD><TR>');});			
		},
    });
});

function searchUsers(key) {
	$.ajax({
				type : "GET",
				url : "users/searchUser?key=" + $("#search").val(),
				dataType : 'json',
				success : function(data) {
					$("#informationTable").html('');
					$("#informationTable").html('<TR><TD>姓名</TD><TD>电话</TD></TR>');
					$(data.userList).each(function(i, value) {
						$("#informationTable").html($("#informationTable").html()
						+'<TR><TD>'+ value.userName+'</TD><TD>'+value.telephone+'</TD><TD>'+
						'<input type="button" style="float:right" value="删除" class="btn btn-primary"'+
						' onclick="deleteUsers('+value.id+',this)"></TD><TR>');});			
				},
		    });
		};
		
function deleteUsers(id,obj){
	$.ajax({
		type : "GET",
		url : "users/deleteUser?id=" + id,
		dataType : 'json',
		success : function() {
			var node= obj.parentNode.parentNode;
			node.parentNode.removeChild(node);
		},
    });
};

function addUsers(){
	var name = $("#userName").val();
	var telephone = $("#userTelephone").val();
	$.ajax({
		type : "GET",
		url : "users/addUser",
		data : {
			name : name,
			telephone : telephone,
        },
        contentType:"charset=UTF-8",
		success : function() {
			location.href="/home";
		},
    });
};


