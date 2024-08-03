const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url)
  .then((res) => {
    if (!res.ok) throw Error(`HTTP error ${res.status}`);
    return res.json();
  })
  .then((data) => {
    const helloElem = document.getElementById('hello');
    helloElem.textContent = data.hello;
  })
  .catch((err) => console.error('error', err));
