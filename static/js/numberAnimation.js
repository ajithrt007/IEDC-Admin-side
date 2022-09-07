const counters = document.querySelectorAll('.number');
const speed = 200;
counters.forEach(counter=> {
    const updateCount = () =>{
        const target = +counter.getAttribute('data-n');
        const targetFinal = target;
        const count= +counter.innerText;
        const inc = target/speed;
        if (count<target){
            counter.innerText = Math.ceil(count + inc);
            setTimeout(updateCount,1);
        }
        else{
            counter.innerText = targetFinal;
        }
    }
    updateCount();
});


































// $(function () {
//     var fx = function fx() {
//     $(".number").each(function (i, el) {
//         var data = parseInt(this.dataset.n, 10);
//         var props = {
//             "from": {
//                 "count": 0
//             },
//                 "to": { 
//                 "count": data
//             }
//         };
//         $(props.from).animate(props.to, {
//             duration: 1000 * 1,
//             step: function (now, fx) {
//                 $(el).text(Math.ceil(now));
//             },
//             complete:function() {
//                 if (el.dataset.sym !== undefined) {
//                   el.textContent = el.textContent.concat(el.dataset.sym)
//                 }
//             }
//         });
//     });
//     };
    
//     var reset = function reset() {
//         //console.log($(this).scrollTop())
//         if ($(this).scrollTop() > 90) {
//             $(this).off("scroll");
//           fx()
//         }
//     };
    
//     $(window).on("scroll", reset);
// });