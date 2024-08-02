// const myList = document.getElementsByClassName('my_list')[0];
// const myList = document.querySelector('ul');
const myList = document.querySelector('.my_list');
const addItem = document.getElementById('add_item');

addItem.onclick = () => {
  const newli = document.createElement('li');
  newli.textContent = 'Item';
  //  newli.innerHTML = 'Item'; serviría <b>Item</b>
  myList.appendChild(newli);
};
