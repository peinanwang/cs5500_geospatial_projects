const menu = document.querySelector('#mobile_menu');
const menuLink = document.querySelector('.navbar_menu');

menu.addEventListener('click', function() {
  menu.classList.toggle('is-active');
  menuLink.classList.toggle('active');
})