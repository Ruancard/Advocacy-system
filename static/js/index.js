const menu = document.querySelector('.menu')
const texto = document.querySelector('.texto')

menu.addEventListener('mouseenter', () => 
texto.classList.toggle('texto--ativo'))

menu.addEventListener('mouseleave', () => 
texto.classList.toggle('texto--ativo'))