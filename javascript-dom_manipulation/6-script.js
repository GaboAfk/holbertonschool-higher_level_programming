const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then((res) => {
    if (!res.ok) throw Error(`HTTP error: ${res.status}`);
    return res.json();
  })
  .then((data) => {
    const character = document.getElementById('character');
    character.textContent = data.name;
  });
