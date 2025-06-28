
let currentPath = window.location.pathname;

const links = document.querySelectorAll('li a');

links.forEach(link => {
    const linkPath = (link.getAttribute('href')).toLowerCase()
    const regex = /^\/[^\/]+\/([^\/]+)\//;
    const match_path = currentPath.match(regex);
    const match_link = linkPath.match(regex)
    if (match_path !== null && match_link !== null) {
        if (match_path[1] === match_link[1]) {
            link.classList.add('active')
        }
    }
});

let btns = document.querySelectorAll("li a")

function give_classes(btns) {
    for (let a = 0; a < btns.length; a++) {
        btns[a].classList.add('nav_btn')
    }
}

give_classes(btns)

btns.forEach(button => {
    button.addEventListener('click', event => {
    for (let a = 0; a < btns.length; a++) {
        if (btns[a].classList.contains('active')) {
            btns[a].classList.remove('active')
        }
    }
    button.classList.add('active')
  });
});




