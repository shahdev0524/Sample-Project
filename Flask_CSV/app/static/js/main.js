$('#flight_search').click(function () {
	vFrom=document.getElementById('Origin').value
	vDestination=document.getElementById('destination').value
    $.ajax({
        url: "deltaairline?origin=" + vFrom + "&dest=" + vDestination,
        type: "GET",
        dataType: 'json',
		contentType: 'application/json',
        success: function (data, xhr, status) {
        	console.log(data)
        	
        	var trHTML = '';
		    $.each(data, function (i, item) {
		        trHTML += '<tr><td>' + data[i].flt_num+ '</td><td>' + data[i].origin + '</td><td>' + data[i].origin_full_name + '</td><td>' + data[i].destination + '</td><td>' + data[i].destination_full_name + '</td></tr> ';
		    });
		    $('#flightdata').empty();
		    $('#flightdata').append(trHTML);
        },
        error: function (xhr, status) {
            alert("Oops, there is a problem!! Please contact to technical team!!");
        }
    });
});