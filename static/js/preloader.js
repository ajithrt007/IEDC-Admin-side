var loader = document.querySelector(".page-loader");
body.style.overflowY = "hidden";
window.addEventListener("load",function(){
    loader.style.display = "none";
    body.style.overflowY = "unset";
});
