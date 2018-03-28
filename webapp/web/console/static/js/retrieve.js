function show(){
    var deviceId = document.getElementById("deviceId").value;
    var url = 'ajax_data_retrieve/?deviceID=' + deviceId;
    //$("#result_panel").append(' <p class="h1"> this is the result in table form</p>');
    $.getJSON(url,function (ret) {
        //alert(ret);
        if(ret=='false'){
            alert('The device has no data!');
            window.open('retrieve.html','_self');
        }else{
            for (var i = 0; i < ret.length; i++) {
                $("#result").append('<br>' + ret[i]);
            }
            $("#information").html('<thead><tr>' +
                '<th>DeviceID</th>' +
                '<th>Temperature</th>' +
                '<th>Humidity</th>' +
                '<th>Light</th>' +
                '<th>Day</th>' +
                '<th>Time</th>' +
                '</tr></thead>');
            $('#information').append('<tbody>');

            for (var i = 0; i < ret.length; i++) {
                $('#information').append('<tr class="info"><td>' + ret[i][0] + '</td><td>' + ret[i][1] + '</td>'
                    + '<td>' + ret[i][2] + '</td>' + '<td>' + ret[i][3] + '</td>' + '<td>' + ret[i][4] + '</td>'
                    + '<td>' + ret[i][5] + '</td></tr>');

            }
        }
    });



}