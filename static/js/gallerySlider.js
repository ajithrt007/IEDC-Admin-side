const carousel = document.querySelector('.carousel1');
const rightArrow = document.querySelector('.right');
const leftArrow = document.querySelector('.left');
// rightArrow.addEventListener("click",(e)=>{
//     carousel.scrollLeft = 425;
// });
// leftArrow.addEventListener("click",(e)=>{
//     carousel.scrollLeft = -425;
// });
function scrollLeft(){
    carousel.scrollLeft = -425;
}
function scrollRight(){
    carousel.scrollLeft = 425;
}