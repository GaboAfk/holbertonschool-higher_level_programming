const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then((res) => {
    if (!res.ok) throw Error(`HTTP error ${res.status}`);
    return res.json();
  })
  .then((data) => {
    const listMovies = document.getElementById('list_movies');
    data.results.forEach((movie) => {
      const newli = document.createElement('li');
      newli.textContent = movie.title;
      listMovies.appendChild(newli);
    });
  })
  .catch((err) => console.error('Error fetching movies:', err));
