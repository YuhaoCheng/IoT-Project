function logIn(){
    var user_name = document.getElementById("username").value; // without value, it's an object
    var password = document.getElementById("password").value;
    $.getJSON('check',function (ret) {
        //alert(ret[0][0]);
        for(var i = 0;i<ret.length;i++){
            if(ret[i][0] == user_name){
                if(ret[i][1] == password){
                    window.open('manage.html','_self');
                    break;
                }
                else{
                    alert('Error password');
                    break;
                }
            }
        }
        if(i == (ret.length - 1 )){alert('No such manager');}

    });
}

function add_new_device() {
    var device_number = document.getElementById("deviceNumber").value;
    var location = document.getElementById("location").value;
    var type = document.getElementById("type").value;
    var description = document.getElementById("description").value;
    var url = 'add_new_device/?deviceID=' + device_number +'&location=' + location + '&type=' + type + '&description=' + description;
    var flag = true;
    var warningMessage ='';
    if(device_number==''||location==''||type==''||description==''){
        //alert("Error!!");
        warningMessage = warningMessage +'Error!\n';
        if(device_number==''){
            warningMessage += 'The device number is empty! Please enter it!\n';
        }
        if(location==''){
            warningMessage += 'The location is empty! Please enter it!\n';
        }
        if(type==''){
            warningMessage += 'The type is empty! Please enter it!\n';
        }
        if(description==''){
            warningMessage += 'The description is empty! Please enter it!\n';
        }
        alert(warningMessage);
        //window.open('manage.html','_self');
        flag = false;

    }
    if(flag){
        //window.open('manage.html','_self');
        $.getJSON(url,function (ret) {
        // alert("!!!");
        //alert(ret);
        if(ret == "true"){
             alert("Add a new device!!");
             window.open('manage.html','_self');
            // flag = 'True';
        }else{
             alert("The device is existed");
             window.open('manage.html','_self');
            // flag = 'False';
        }
        });
    }else{
        window.open('manage.html','_self');
    }



}

function delete_device() {
    //alert("Delete a device!!");
    var device_number = document.getElementById("deleteDeviceNumber").value;
    var url = 'delete_device/?deviceID=' + device_number;
    $.getJSON(url,function (ret) {
        if(ret == "true"){
             alert("Successfully delete the device");
             window.open('manage.html','_self');
            // flag = 'True';
        }else{
             alert("Can't delete the device");
             window.open('manage.html','_self');
            // flag = 'False';
        }

    });
    //window.open('manage.html','_self');

}