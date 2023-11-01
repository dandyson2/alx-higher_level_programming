// Wait for the document to be fully loaded and ready
$('document').ready(function () {
  // Make an asynchronous GET request to the API endpoint for French greeting
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // Update the text content of the <div> with ID 'hello' to the retrieved French greeting
    $('DIV#hello').text(data.hello);
  });
});
