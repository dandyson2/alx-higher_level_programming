// Make an asynchronous GET request to the Star Wars API endpoint for character ID 5
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  // Update the text content of the <div> with ID 'character' to the retrieved character's name
  $('DIV#character').text(data.name);
});
