var prevgoto;
var prevScroll;
var animating = false;
$(function () {
  var links = document.querySelectorAll("a");
  for (var i = 0; i < links.length; i++) {
    for (var j = 0; j < links[i].classList.length; j++) {
      if (links[i].classList[j] == "animate-scroll") {
        links[i].addEventListener("click", function (event) {
          var goto = this.getAttribute('href');
          var oldScroll = $(window).scrollTop();
          var newScroll = $(goto).offset().top - 119;
          if (prevgoto !== goto || (!animating && Math.floor(prevScroll) !== Math.floor(oldScroll))) {
            animating = true;
            $('html, body').animate({
              scrollTop: newScroll
            }, 1000);
            var timer;
            clearTimeout(timer);
            timer = setTimeout(function () {
              animating = false;
            }, 1000);
          }
          prevgoto = goto;
          prevScroll = newScroll;
          scrolled = 0;
          if ($(window).width() < 768) {
            if (goto != "#body" && this.id != "scroll") {
              document.querySelector("button").click();
            } else if (goto == "#body") {
              checkButtonAndClick();
            }
          }
        });
      }
    }
  }
});

