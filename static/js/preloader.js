var scroll_y;
var loader = document.querySelector(".page-loader");
window.addEventListener("scroll", function(event) {  
    var scroll_y = this.scrollY;
    loader.style.top = scroll_y + 'px';
});
body.style.overflowY = "hidden";
window.addEventListener("load",function(){
    loader.style.display = "none";
    body.style.overflowY = "unset";
});
