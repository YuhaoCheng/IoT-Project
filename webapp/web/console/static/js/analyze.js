function plt() {
    var deviceId = document.getElementById("deviceId").value;
    var attribute = document.getElementById("attribute").value;
    var location = 0; // default the figure is temperature-time figure
    /*
    Base on the value of attribute to choose which elements will be put in the buffer[]
    Temperature is ret[0],
    Humidity is ret[1],
    Light is ret[2]
     */
    if(attribute == "Temperature"){
        location = 0;
    }

    if(attribute == "Humidity"){
        location = 1;
    }

    if(attribute == "Light"){
        location = 2;
    }

    var url = 'ajax_data_analyze/?deviceID=' + deviceId;
    var buffer = Array();
    var time = Array();
    $.getJSON(url,function (ret) {
        for(var i = 0;i <ret.length;i++) {
            buffer.push(ret[i][location]);
            //$("#data-point").append('<p>'+buffer[i]+'</p>');
            time.push(ret[i][3]);
            //$("#x-point").append('<p>'+time[i]+'</p>');
            //$("#x-point").append('<p>'+time[i]+'</p>');
            var trace1 = {
                x: time,
                y: buffer,
                type: 'scatter'
            };

            var data = [trace1];
            Plotly.newPlot('figure',data);

        }

    });

    // var trace1 = {
    //     x: temperature,
    //     y: time,
    //     type: 'scatter'
    // };
    //
    // var data = [trace1]
    // Plotly.newPlot('test',data);


}

