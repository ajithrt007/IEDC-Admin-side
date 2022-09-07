const carousel = document.querySelector('.carousel1');
const maxWidth = carousel.scrollWidth;
const rightArrow = document.querySelector('.right');
const leftArrow = document.querySelector('.left');
var scrollValue = 0;
// rightArrow.addEventListener("click",function(){
//     scrollValue++;
//     console.log(scrollValue);
//     carousel.scrollLeft = ((scrollValue *  425) <= maxWidth)?scrollValue *  425: 0 ;
// });
// leftArrow.addEventListener("click",function(){
//     scrollValue--;
//     console.log(scrollValue);
//     carousel.scrollLeft = ((scrollValue *  -425) >= 0)?scrollValue *  -425: 0 ;
// });

rightArrow.addEventListener("click",function(){
    scrollValue = (scrollValue <= 10)? scrollValue++ : scrollValue;
    console.log(scrollValue);
    carousel.scrollLeft = scrollValue *  425;
});
leftArrow.addEventListener("click",function(){
    scrollValue = (scrollValue > 0)? scrollValue-- : scrollValue;
    console.log(scrollValue);
    carousel.scrollLeft = (10 - scrollValue) *  -425;
});