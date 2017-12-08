
function searchImage()
{

    alert("4");
    var fileSystem = new ActiveXObject("Scripting.FileSystemObject");
    alert("5");
    var imageDir = fileSystem.GetFolder("../image");
    alert("6");
    var imageFiles = new Enumerator(imageDir.files);

    return imageFiles;
}

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
    var imageFiles = searchImage();
    alert("2");
    addImg(imageFiles);
    alert("3");
}