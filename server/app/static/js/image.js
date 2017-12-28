function addImg(imageFiles)
{
    var div = document.getElementById('imageDiv');
    var i = 0;
    for(;i<imageFiles.length;i++)
    {
        var img = document.createElement("img");
        img.setAttribute("class","image");
        img.src = "../static/image/259/7/" + imageFiles[i];
        div.appendChild(img);
    }
}

function start()
{
}

function checkimage(image,noimage){

    image.push("1");
    image.push("2");
    noimage.push("3");
    noimage.push("4");
}

var flag = false;

function ajaxpost(json){

    $.ajax({
        url: '/ajaxpost',
        data:JSON.stringify(json),
        contentType: 'application/json;charset=UTF-8',
        type:'POST',
        success:function(response){
            var files = response["files"];
            addImg(files);
            flag = true;
        },
        error:function(){

        }
    });
    
}

$(document).ready(function(){

    var image = [];
    var noimage = [];

    var json = {};
    checkimage(image,noimage);

    json["image"] = image;
    json["noimage"] = noimage;
    ajaxpost(json);
    if(flag)
    {
        flag = false;
    }

});