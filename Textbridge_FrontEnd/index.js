$(document).ready(function () {
    var scrolled = 0;
    $(function () {
      $(document).scroll(function () {
        var $nav = $("#main-navbar");
        scrolled = 1;
        $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
    });
})});