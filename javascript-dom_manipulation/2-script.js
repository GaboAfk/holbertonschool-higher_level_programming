const redHeader = document.getElementById('red_header');
const header = document.querySelector('header');

redHeader.onclick = () => {
  header.classList.add('red');
};
