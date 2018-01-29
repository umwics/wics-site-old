function positionFooter() {
    var docHeight = $(document).height();
    var viewportHeight = $(window).height();

    if (docHeight <= viewportHeight) {
        $('#footer-navbar').addClass('navbar-fixed-bottom');
    }
}


