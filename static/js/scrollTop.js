// function topFunction() {
//     document.body.scrollTop = 0; // For Safari
//     document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
// }

// $(function () {
//   "use strict";

//   $(window).on("scroll", function () {
//     if ($(this).scrollTop() > 100) {
//     //   $(".scrollTop_top").slideDown();
//     } else {
//       $(".scrollTop_top").slideUp();
//     }
//   });

//   $(".scrollTop_top").on("click", function () {
//     $("html, body").animate({ scrollTop: 0 }, 300);
//     $("html, body").animate({ scrollTop: 40 }, 150);
//     $("html, body").animate({ scrollTop: 0 }, 100);
//     $("html, body").animate({ scrollTop: 20 }, 100);
//     $("html, body").animate({ scrollTop: 0 }, 100);
//     $("html, body").animate({ scrollTop: 10 }, 50);
//     $("html, body").animate({ scrollTop: 0 }, 100);
//     $("html, body").animate({ scrollTop: 5 }, 50);
//     $("html, body").animate({ scrollTop: 0 }, 100);
//   });
// });

$(window).on("scroll", function () {
    if (window.scrollY > window.outerHeight) {
      $("#scrollToTop").addClass("active");
      setTimeout(function() {
        var theta = ($(window).scrollTop() - (window.outerHeight + (window.outerHeight/2))) / 500;
        $('#scrollToTop').css({ transform: 'rotate(' + theta + 'rad)' });
      })
    } else {
      $("#scrollToTop").removeClass("active");
    }
  });

  $('#scrollToTop').on('click',function() {
    $("html, body").animate({ scrollTop: 0 }, 500);
  })
