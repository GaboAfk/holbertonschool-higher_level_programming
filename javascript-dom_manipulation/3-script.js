const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.onclick = () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
};

/* toggleHeader.onclick = () => {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
}; */
