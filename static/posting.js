function set_image(data){            
    var blobData = data;
    var url = window.URL || window.webkitURL;
    var src = url.createObjectURL(data);
    $('#ID_result').attr("src", src);
}

function poster_func() {
	color_data = {"r": $("#ID_r").val(), "g": $("#ID_g").val(), "b": $("#ID_b").val()}
	$.ajax({
		type: "POST",
        url: '/post_catcher',
        data: color_data,
        xhrFields:{
            responseType: 'blob'
        },
        success: set_image
	});
}

