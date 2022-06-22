// const carousel = document.querySelector('.carousel');
// let initialPos = null;
// let moving = false;
// window.addEventListener('mousedown',(e)=>{
//     initialPos = e.pageX;
//     moving = true;
//     const transformMatrix = window.getComputedStyle(carousel).getPropertyValue('transform');
//     if(transformMatrix !== 'none'){
//         transform = parseInt(transformMatrix.split(',')[4].trim());
//     }
// });
// window.addEventListener('mousemove',(e)=>{
//     if(moving){
//         const currentPos = e.pageX;
//         const diff = currentPos - initialPos;       
//         carousel.style.transform = "translateX(" + diff + "px)";
//     }
// });
// window.addEventListener('mouseup',(e)=>{
//     moving = false;
// });
