function upload() {
    alert("asdf");
    var form_data = new FormData();
    var file_info = $('#file_upload')[0].files[0];
    form_data.append('file',file_info);
    //if(file_info==undefined)暂且不许要判断是否有附件
    //alert('你没有选择任何文件');
    //return false
    //}

    // 提交ajax的请求
    $.ajax({
        url:"/adminweb/file_upload/",
        type:'POST',
        data: form_data,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function(res) {
            var obj = JSON.parse(res);
            if (obj.status) {
                alert(obj.data);
                $('#img').attr("src",obj.data);
            }
        }
    }); // end ajax
}
