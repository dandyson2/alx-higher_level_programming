// Attach a click event handler to the <div> element with ID 'update_header'
$('DIV#update_header').click(function () {
  // When the <div> is clicked, update the text content of <header> to 'New Header!!!'
  $('HEADER').text('New Header!!!');
});
