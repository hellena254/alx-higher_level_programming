$(document).ready(function() {
  $('#ass_item').click(function() {
    var newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });
});
