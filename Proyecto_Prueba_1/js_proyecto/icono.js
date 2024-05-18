$(document).ready(function () {

  /* Epica funcion para ir hacia arriba */
  $(window).scroll(function() {
    var scrollTop = $(window).scrollTop();
    var btnVolverArriba = $("#scrollToTopBtn");

    if (scrollTop > 100) {
      btnVolverArriba.fadeIn(300);
    } else {
      btnVolverArriba.fadeOut(300);
    }
  });
  
  $("#scrollToTopBtn").click(function () {
    $("html, body").animate({ scrollTop: 0 }, "slow");
  });


});
