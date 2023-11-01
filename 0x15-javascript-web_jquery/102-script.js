$(document).ready(function () {
  // When the document is ready, this function is executed

  const url = 'https://www.fourtonfish.com/hellosalut/?';
  // The URL endpoint for fetching translation data is stored in the 'url' variable

  $('INPUT#btn_translate').click(function () {
    // When the 'INPUT#btn_translate' element is clicked, this function is executed

    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      // A GET request is sent to the specified URL with the selected language code as a parameter

      $('DIV#hello').html(data.hello);
      // The translated greeting received from the API response is displayed in the 'DIV#hello' element
    });
  });
});
