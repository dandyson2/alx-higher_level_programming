$(document).ready(function () {
  // When the document is ready, this function is executed
  $('DIV#add_item').click(function () {
    // When the 'DIV#add_item' element is clicked, this function is executed
    $('UL.my_list').append('<li>Item</li>');
    // It appends a new 'li' element with the text "Item" to the 'UL.my_list'
  });

  $('DIV#remove_item').click(function () {
    // When the 'DIV#remove_item' element is clicked, this function is executed
    $('UL.my_list li:last').remove();
    // It removes the last 'li' element within the 'UL.my_list'
  });

  $('DIV#clear_list').click(function () {
    // When the 'DIV#clear_list' element is clicked, this function is executed
    $('UL.my_list').empty();
    // It empties (removes all content from) the 'UL.my_list'
  });
});
