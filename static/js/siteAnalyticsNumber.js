// const counter = document.querySelectorAll('.number-numberdata');
// const speedn = 300;
// counter.forEach(counter=> {
//     const updateCount1 = () =>{
//         const target = +counter.getAttribute('data-n');
//         const targetFinal = target;
//         const count= +counter.innerText;
//         const inc = target/speedn;
//         if (count<target){
//             counter.innerText = Math.ceil(count + inc);
//             setTimeout(updateCount1,1);
//         }
//         else{
//             counter.innerText = targetFinal;
//         }
//     }
//     updateCount1();
// });
$(document).ready(function(){
    $(".number-numberdata").counterUp({
        delay:10,
        time:1200
    });
});