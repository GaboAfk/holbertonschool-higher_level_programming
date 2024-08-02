const header = document.querySelector('header');
const updateHeader = document.getElementById('update_header');

updateHeader.onclick = () => {
  header.textContent = 'New Header!!!';
};
