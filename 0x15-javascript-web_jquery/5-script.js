// When the element with ID 'add_item' is clicked,
// add a new list item with the text 'Item' to the unordered list with class 'my_list'.
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
