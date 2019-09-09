function download_func() {
    color_data = {"r": $("#ID_r").val(), "g": $("#ID_g").val(), "b": $("#ID_b").val()}
    console.log("hello")
    $.redirect("/download", color_data)
}

