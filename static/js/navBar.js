var menu = document.getElementById('menu');
var body = document.getElementById('theBody');
function openMenu(){
    menu.style.display = 'block';
    body.style.overflowY = 'hidden';
}
function closeMenu(){
    menu.style.display = 'none';
    body.style.overflowY = 'unset';
}