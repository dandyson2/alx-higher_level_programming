// Make an asynchronous GET request to the Star Wars API endpoint for films
$.get('https://swapi.co/api/films/?format=json', function (data) {
  // Map through the results and create a list of movie titles using template literals
  const movieTitles = data.results.map(movie => `<li>${movie.title}</li>`);
  
  // Append the movie titles list to the <ul> element with ID 'list_movies'
  $('UL#list_movies').append(...movieTitles);
});
