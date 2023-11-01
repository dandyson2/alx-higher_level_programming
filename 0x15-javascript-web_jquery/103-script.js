// Wait for the document to be fully loaded and ready
$('document').ready(function () {
  // Attach click event handler to the element with ID 'btn_translate'
  $('INPUT#btn_translate').click(translate);
  
  // Attach focus event handler to the element with ID 'language_code'
  $('INPUT#language_code').focus(function () {
    // Attach keydown event handler to the 'language_code' input field
    $(this).keydown(function (e) {
      // Check if the pressed key is Enter (keyCode 13)
      if (e.keyCode === 13) {
        // If Enter key is pressed, call the translate function
        translate();
      }
    });
  });
});

// Function to translate text based on the language code input
function translate () {
  // API endpoint URL for translation
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  
  // Make a GET request to the API with the language code as a parameter
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    // Update the content of the element with ID 'hello' with the translated text
    $('DIV#hello').html(data.hello);
  });
}
