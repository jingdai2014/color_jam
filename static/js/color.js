$('.colors > .color-group > div > .unsel').on({
  mouseover: function() {
    $(this).animate({
      width: 80,
      height: 80,
      margin: -15,
    }, 100, function() {
        $(this).css('z-index', '2');
      });
    $(this).on('mouseleave', function() {
      $(this).animate({
        width: 50,
        height: 50,
        margin: 0,
      }, 100, function() {
        $(this).css('z-index', '1');
      });
    });
  },
  mouseleave: function() {
    $(this).animate({
      width: 50,
      height: 50,
      margin: 0,
    }, 100, function() {
      $(this).css('z-index', '1');
    });
  },
  click: function() {
    $('.colors > .color-group > div > .unsel').css({
      'width': '50px',
      'height': '50px',
      'margin': '0px',
      'z-index': '1'
    })
    $(this).css({
      'width': '80px',
      'height': '80px',
      'margin': '-15px',
      'z-index': '2'
    })
    $(this).off('mouseleave');
    $('.color-text').text($(this).css("background-color"));
    $('.logo > img').css('background-color', $(this).css("background-color"))
  }
});