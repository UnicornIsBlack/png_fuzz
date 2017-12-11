function addImg(imageFiles)
{
    var div = document.getElementsByClassName("imageDiv")[0];

    while( !imageFiles.atEnd() )
    {
        var img = document.createElement("img");
        img.setAttribute("class","image");
        img.src = "../image/" + imageFiles.item();
        div.appendChild(img);
        imageFiles.moveNext();
    }
}

function start()
{
    alert("1");
}

$(document).ready(function(){
    var car = [];
    car.push("1");
    car.push("2");
})