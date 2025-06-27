
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
        if (button.classList.contains('active')) {
            button.classList.remove('active')
        }
    }
    button.classList.add('active')

  });
});

