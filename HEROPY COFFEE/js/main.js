const searchEl = document.querySelector('.search');
const searchInputEl = searchEl.querySelector('.input');
searchEl.addEventListener('click', function () {
    searchInputEl.focus();
});
searchEl.addEventListener('focus', function () {
    searchEl.classList.remove('focusde');
    searchInputEl.setAttribute('placeholder', '');
});
const badgeEl = document.querySelector('header .badges');

window.addEventListener('scroll', function () {
    console.log(window.scrollY);
    if (window.scrollY > 500) {
        badgeEl.style.display = 'none';
    } else {
        badgeEl.style.display = 'block';
    }
});